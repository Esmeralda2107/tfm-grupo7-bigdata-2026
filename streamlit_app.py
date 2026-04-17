
from pathlib import Path
import json
import pandas as pd
import plotly.express as px
import streamlit as st


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="TFM GRUPO 7 SITE SELECTION MANHATTAN",
    page_icon="📍",
    layout="wide",
)

def find_repo_root(start_path: Path) -> Path:
    for candidate in [start_path, *start_path.parents]:
        if (candidate / "datos").exists() and (candidate / "resultados").exists():
            return candidate
    return start_path

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = find_repo_root(APP_DIR)

WARD_PATH = REPO_ROOT / "resultados" / "04_clustering" / "Ward.D" / "manhattan_Ward_k4.xlsx"
MICRO_PATH = REPO_ROOT / "resultados" / "05_scoring" / "scoring_micro.csv"
MACRO_PATH = REPO_ROOT / "resultados" / "05_scoring" / "scoring_macro.csv"
CONSOLIDADO_PATH = REPO_ROOT / "resultados" / "06_escenarios" / "consolidado_escenarios.csv"
GEOJSON_DIR = REPO_ROOT / "datos" / "crudos" / "zonas"


# =========================================================
# ESTILOS
# =========================================================
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 16px 18px;
        min-height: 132px;
    }
    .metric-title {
        font-size: 0.90rem;
        color: #475569;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        line-height: 1.25;
        word-wrap: break-word;
        overflow-wrap: anywhere;
    }
    .metric-sub {
        font-size: 0.85rem;
        color: #64748b;
        margin-top: 8px;
    }
    .scenario-box {
        background-color: #f1f5f9;
        border-left: 4px solid #0f766e;
        padding: 12px 14px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .note-box {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 12px;
    }
    .summary-box {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 14px;
        padding: 16px;
        margin-top: 14px;
        margin-bottom: 10px;
    }
    .group-title {
        margin-top: 18px;
        margin-bottom: 8px;
        font-weight: 700;
        color: #0f172a;
        font-size: 1.03rem;
    }
    .custom-table table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.92rem;
    }
    .custom-table th, .custom-table td {
        border: 1px solid #e2e8f0;
        padding: 8px 10px;
        text-align: left !important;
        vertical-align: top;
    }
    .custom-table th {
        background-color: #f1f5f9;
        font-weight: 700;
    }
    .custom-table thead tr:nth-child(1) th {
        text-align: center !important;
        background-color: #e2e8f0;
    }
    .custom-table thead tr:nth-child(2) th {
        text-align: left !important;
        background-color: #f1f5f9;
    }
    .chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 8px 0 14px 0;
    }
    .chip {
        background: #f1f5f9;
        color: #0f172a;
        border: 1px solid #cbd5e1;
        border-radius: 999px;
        padding: 6px 10px;
        font-size: 0.85rem;
        white-space: nowrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# METADATOS DEL MODELO
# =========================================================
DIMENSIONS = {
    "DEMANDA": {
        "label": "Censo (Demanda)",
        "variables": {
            "POBLACION_KM2": {"label": "Población por km²", "weight": 30},
            "PORCENTAJE_HISPANOS": {"label": "Porcentaje hispanos", "weight": 20},
            "EDAD_MEDIANA": {"label": "Edad mediana", "weight": 10},
            "INGRESO_MEDIANO_HOGAR": {"label": "Ingreso mediano del hogar", "weight": 25},
            "TAMANO_HOGAR_PROMEDIO": {"label": "Tamaño hogar promedio", "weight": 15},
        },
    },
    "MOVILIDAD": {
        "label": "Movilidad",
        "variables": {
            "MOVILIDAD_PROMEDIO_DIARIA": {"label": "Movilidad promedio diaria", "weight": 80},
            "MOV_CANTIDAD_ESTACIONES": {"label": "Cantidad de estaciones", "weight": 20},
        },
    },
    "SEGURIDAD": {
        "label": "Seguridad",
        "variables": {
            "DELITO_PROPIEDAD_KM2": {"label": "Delito propiedad por km²", "weight": 45},
            "DELITO_TRANSPORTE_KM2": {"label": "Delito transporte por km²", "weight": 35},
            "DELITO_OTROS_KM2": {"label": "Otros delitos por km²", "weight": 20},
        },
    },
    "PTOS_INTERES": {
        "label": "Puntos de interés",
        "variables": {
            "LUGARES_COMERCIO_KM2": {"label": "Lugares comercio por km²", "weight": 35},
            "LUGARES_OFICINAS_KM2": {"label": "Lugares oficinas por km²", "weight": 45},
            "LUGARES_RESIDENCIAL_KM2": {"label": "Lugares residencial por km²", "weight": 20},
        },
    },
    "COMPETENCIA": {
        "label": "Competencia",
        "variables": {
            "COMPETENCIA_DIRECTA_KM2": {"label": "Competencia directa por km²", "weight": 90},
            "COMPETENCIA_INDIRECTA_KM2": {"label": "Competencia indirecta por km²", "weight": 10},
        },
    },
    "COSTE": {
        "label": "Coste",
        "variables": {
            "ALQ_PRECIO_PIE2_ANUAL": {"label": "Precio alquiler pie² anual", "weight": 100},
        },
    },
}

SCENARIOS = {
    "Potencial de demanda": {
        "description": "Prioriza las dimensiones más vinculadas con la capacidad de atracción comercial de la zona.",
        "weights": {
            "DEMANDA": 35,
            "PTOS_INTERES": 25,
            "MOVILIDAD": 15,
            "SEGURIDAD": 10,
            "COSTE": 10,
            "COMPETENCIA": 5,
        },
        "main_dims": ["DEMANDA", "PTOS_INTERES"],
        "context_dims": ["MOVILIDAD", "SEGURIDAD", "COSTE", "COMPETENCIA"],
    },
    "Eficiencia y flujo": {
        "description": "Da mayor peso a las condiciones urbanas más relevantes para un modelo fast casual orientado al take-away.",
        "weights": {
            "MOVILIDAD": 35,
            "PTOS_INTERES": 25,
            "DEMANDA": 15,
            "SEGURIDAD": 10,
            "COSTE": 10,
            "COMPETENCIA": 5,
        },
        "main_dims": ["MOVILIDAD", "PTOS_INTERES"],
        "context_dims": ["DEMANDA", "SEGURIDAD", "COSTE", "COMPETENCIA"],
    },
    "Viabilidad y riesgo": {
        "description": "Enfatiza los factores que inciden con mayor fuerza en la estabilidad operativa y económica de la implantación, así como en la saturación competitiva del entorno.",
        "weights": {
            "SEGURIDAD": 20,
            "COSTE": 25,
            "COMPETENCIA": 15,
            "DEMANDA": 15,
            "MOVILIDAD": 10,
            "PTOS_INTERES": 15,
        },
        "main_dims": ["SEGURIDAD", "COSTE", "COMPETENCIA"],
        "context_dims": ["DEMANDA", "MOVILIDAD", "PTOS_INTERES"],
    },
}

CLUSTER_LABELS = {
    1: "Cluster 1",
    2: "Cluster 2",
    3: "Cluster 3",
    4: "Cluster 4",
}

CLUSTER_DIM_DESCRIPTORS = {
    "DEMANDA": "demanda",
    "MOVILIDAD": "movilidad",
    "SEGURIDAD": "seguridad",
    "PTOS_INTERES": "puntos de interés",
    "COMPETENCIA": "competencia",
    "COSTE": "coste",
}


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def metric_card(title, value, subtitle=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-sub">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chips(items):
    html = '<div class="chip-row">'
    for item in items:
        html += f'<span class="chip">{item}</span>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def clean_zone_id(value):
    if pd.isna(value):
        return None
    return str(value).strip().upper()


def fmt_num(x, decimals=2):
    if pd.isna(x):
        return ""
    return f"{x:,.{decimals}f}"


def fmt_int(x):
    if pd.isna(x):
        return ""
    return f"{int(x):,}"


def classify_level(score):
    if score >= 85:
        return "muy alta"
    if score >= 70:
        return "alta"
    if score >= 40:
        return "media"
    if score >= 25:
        return "baja"
    return "muy baja"


def classify_level_plural(score):
    if score >= 85:
        return "muy altas"
    if score >= 70:
        return "altas"
    if score >= 40:
        return "medias"
    if score >= 25:
        return "bajas"
    return "muy bajas"


def score_icon(score):
    if score >= 85:
        return "🟢"
    if score >= 70:
        return "🟩"
    if score >= 40:
        return "🟡"
    if score >= 25:
        return "🟠"
    return "🔴"


def detect_geojson_id_field(geojson_dict):
    features = geojson_dict.get("features", [])
    if not features:
        return None
    props = features[0].get("properties", {})
    candidates = ["NTA2020", "nta2020", "NTACode", "NTA_CODE", "nta_code", "NTA", "nta", "id", "ID"]
    for cand in candidates:
        if cand in props:
            return cand
    return list(props.keys())[0] if props else None


def extract_geojson_ids(geojson_dict, geo_field):
    ids = []
    for feature in geojson_dict.get("features", []):
        props = feature.get("properties", {})
        ids.append(clean_zone_id(props.get(geo_field)))
    return ids


@st.cache_data
def load_data():
    required_paths = [WARD_PATH, MICRO_PATH, MACRO_PATH, CONSOLIDADO_PATH]
    missing_files = [p for p in required_paths if not p.exists()]
    if missing_files:
        raise FileNotFoundError(
            "Faltan archivos necesarios para la app:\n" + "\n".join(str(p) for p in missing_files)
        )

    geojson_files = sorted(GEOJSON_DIR.glob("*.geojson"))
    if not geojson_files:
        raise FileNotFoundError(f"No se encontró ningún .geojson dentro de: {GEOJSON_DIR}")

    raw_df = pd.read_excel(WARD_PATH)
    micro_df = pd.read_csv(MICRO_PATH)
    macro_df = pd.read_csv(MACRO_PATH)
    consolidado_df = pd.read_csv(CONSOLIDADO_PATH)

    with open(geojson_files[0], "r", encoding="utf-8") as f:
        geojson = json.load(f)

    return raw_df, micro_df, macro_df, consolidado_df, geojson


def validate_columns(df):
    required = [
        "ID_ZONA", "NOMBRE_ZONA", "CLUSTER",
        "DEMANDA", "MOVILIDAD", "SEGURIDAD", "PTOS_INTERES", "COMPETENCIA", "COSTE",
        "SCORE_MEDIO", "RANKING_GLOBAL", "VARIABILIDAD_ENTRE_ESCENARIOS", "CONSISTENCIA_ESCENARIOS",
    ]
    for dim_meta in DIMENSIONS.values():
        required.extend(list(dim_meta["variables"].keys()))
        required.extend([f"SCORE_{v}" for v in dim_meta["variables"].keys()])
    missing = [c for c in required if c not in df.columns]
    return missing


def build_cluster_descriptions(df):
    macro_cols = ["DEMANDA", "MOVILIDAD", "SEGURIDAD", "PTOS_INTERES", "COMPETENCIA", "COSTE"]
    overall = df[macro_cols].mean()
    cluster_names = {}

    for cluster_id in sorted(df["CLUSTER"].dropna().unique()):
        sub = df[df["CLUSTER"] == cluster_id]
        diff = (sub[macro_cols].mean() - overall).sort_values(ascending=False)
        top_dims = [CLUSTER_DIM_DESCRIPTORS[idx] for idx in diff.index[:2]]
        if len(top_dims) >= 2:
            cluster_names[cluster_id] = f"Predominio de {top_dims[0]} y {top_dims[1]}"
        elif len(top_dims) == 1:
            cluster_names[cluster_id] = f"Predominio de {top_dims[0]}"
        else:
            cluster_names[cluster_id] = "Perfil territorial general"
    return cluster_names


def prepare_dataframe(raw_df, micro_df, macro_df, consolidado_df):
    raw = raw_df.copy()
    if "Cluster" in raw.columns:
        raw = raw.rename(columns={"Cluster": "CLUSTER"})

    raw["ID_ZONA"] = raw["ID_ZONA"].apply(clean_zone_id)
    raw["NOMBRE_ZONA"] = raw["NOMBRE_ZONA"].astype(str).str.strip()

    micro = micro_df.copy()
    micro["ID_ZONA"] = micro["ID_ZONA"].apply(clean_zone_id)
    micro = micro.drop(columns=["NOMBRE_ZONA", "CLUSTER"], errors="ignore")

    macro = macro_df.copy()
    macro["ID_ZONA"] = macro["ID_ZONA"].apply(clean_zone_id)
    macro = macro.drop(columns=["NOMBRE_ZONA", "CLUSTER"], errors="ignore")

    cons = consolidado_df.copy()
    cons["ID_ZONA"] = cons["ID_ZONA"].apply(clean_zone_id)
    cons = cons.drop(columns=["NOMBRE_ZONA", "CLUSTER"], errors="ignore")

    df = raw.merge(micro, on="ID_ZONA", how="left")
    df = df.merge(macro, on="ID_ZONA", how="left")
    df = df.merge(cons, on="ID_ZONA", how="left")

    df["CLUSTER"] = pd.to_numeric(df["CLUSTER"], errors="coerce").astype("Int64")
    df["CLUSTER_FILTER"] = df["CLUSTER"].map(CLUSTER_LABELS)

    cluster_desc = build_cluster_descriptions(df)
    df["CLUSTER_DESC"] = df["CLUSTER"].map(cluster_desc)

    # Reconstrucción de score 0-100 de cada subvariable a partir del scoring micro ya ponderado
    for dim_key, dim_meta in DIMENSIONS.items():
        for var, var_meta in dim_meta["variables"].items():
            micro_col = f"SCORE_{var}"
            factor = var_meta["weight"] / 100
            df[f"SCORE0_{var}"] = (df[micro_col] / factor).clip(0, 100).round(2)

    return df


def compute_scenario_scores(df, scenario_weights):
    out = df.copy()
    dim_contrib_cols = []

    for dim_key, dim_weight in scenario_weights.items():
        dim_score_col = dim_key
        dim_contrib_col = f"CONTRIB_SCEN_DIM_{dim_key}"

        out[dim_contrib_col] = out[dim_score_col] * (dim_weight / 100)
        dim_contrib_cols.append(dim_contrib_col)

        for var in DIMENSIONS[dim_key]["variables"].keys():
            micro_score_col = f"SCORE_{var}"
            var_contrib_col = f"CONTRIB_SCEN_VAR_{var}"
            out[var_contrib_col] = (out[micro_score_col] * (dim_weight / 100)).round(4)

    out["SCORE_ESCENARIO"] = out[dim_contrib_cols].sum(axis=1).round(2)
    out["RANK"] = out["SCORE_ESCENARIO"].rank(ascending=False, method="dense").astype(int)
    return out.sort_values(["SCORE_ESCENARIO", "VARIABILIDAD_ENTRE_ESCENARIOS"], ascending=[False, True])


def get_top_subdimensions(row, top_n=3):
    items = []
    for dim_key, dim_meta in DIMENSIONS.items():
        for var, var_meta in dim_meta["variables"].items():
            items.append(
                {
                    "label": var_meta["label"],
                    "dimension": dim_meta["label"],
                    "score0": row[f"SCORE0_{var}"],
                    "contrib": row[f"CONTRIB_SCEN_VAR_{var}"],
                    "var": var,
                }
            )
    items = sorted(items, key=lambda x: x["contrib"], reverse=True)
    return items[:top_n]


def render_html_table(df):
    html = '<div class="custom-table">' + df.to_html(index=False, escape=False) + "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_html_table_multiindex(df):
    html = '<div class="custom-table">' + df.to_html(index=False, escape=False) + "</div>"
    st.markdown(html, unsafe_allow_html=True)


def build_grouped_context(df, scenario_name):
    out = df[[
        "RANK", "RANKING_GLOBAL", "ID_ZONA", "NOMBRE_ZONA", "CLUSTER_FILTER",
        "CLUSTER_DESC", "SCORE_ESCENARIO", "VARIABILIDAD_ENTRE_ESCENARIOS", "CONSISTENCIA_ESCENARIOS"
    ]].head(10).copy()

    out["ESCENARIO"] = scenario_name
    out = out.rename(columns={
        "RANK": "Rank escenario",
        "RANKING_GLOBAL": "Ranking global",
        "ID_ZONA": "ID zona",
        "NOMBRE_ZONA": "Zona",
        "CLUSTER_FILTER": "Cluster",
        "CLUSTER_DESC": "Perfil del cluster",
        "SCORE_ESCENARIO": "Score escenario",
        "VARIABILIDAD_ENTRE_ESCENARIOS": "Variabilidad",
        "CONSISTENCIA_ESCENARIOS": "Consistencia",
        "ESCENARIO": "Escenario",
    })

    out["Rank escenario"] = out["Rank escenario"].apply(fmt_int)
    out["Ranking global"] = out["Ranking global"].apply(fmt_int)
    out["Score escenario"] = out["Score escenario"].apply(lambda x: fmt_num(x, 2))
    out["Variabilidad"] = out["Variabilidad"].apply(lambda x: fmt_num(x, 2))
    return out


def build_grouped_dimensions(df):
    out = df[[
        "RANK",
        "NOMBRE_ZONA",
        "DEMANDA",
        "MOVILIDAD",
        "SEGURIDAD",
        "PTOS_INTERES",
        "COMPETENCIA",
        "COSTE",
    ]].head(10).copy()

    out = out.rename(columns={
        "RANK": "Rank",
        "NOMBRE_ZONA": "Zona",
        "DEMANDA": "Demanda",
        "MOVILIDAD": "Movilidad",
        "SEGURIDAD": "Seguridad",
        "PTOS_INTERES": "Puntos de interés",
        "COMPETENCIA": "Competencia",
        "COSTE": "Coste",
    })

    out["Rank"] = out["Rank"].apply(fmt_int)

    for col in ["Demanda", "Movilidad", "Seguridad", "Puntos de interés", "Competencia", "Coste"]:
        out[col] = out[col].apply(
            lambda x: f"{score_icon(float(x))} puntuación {classify_level(float(x))} | {fmt_num(float(x), 1)}"
        )

    return out


def build_grouped_subdimensions(df):
    data_cols = []
    col_tuples = [("", "Rank"), ("", "Zona")]

    for dim_key, dim_meta in DIMENSIONS.items():
        for var, var_meta in dim_meta["variables"].items():
            data_cols.append(var)
            col_tuples.append((dim_meta["label"], var_meta["label"]))

    base = df[["RANK", "NOMBRE_ZONA"] + data_cols].head(10).copy()
    base["RANK"] = base["RANK"].apply(fmt_int)

    for col in data_cols:
        base[col] = base[col].apply(lambda x: fmt_num(x, 2))

    base.columns = pd.MultiIndex.from_tuples(col_tuples)
    return base


def compute_feasible_bounds(total, dims_count, min_each, max_each):
    lower = max(min_each, total - (dims_count - 1) * max_each)
    upper = min(max_each, total - (dims_count - 1) * min_each)
    return lower, upper


def allocate_remaining(selected_dim, selected_value, dims, total, min_each, max_each, base_weights):
    remaining_dims = [d for d in dims if d != selected_dim]
    remaining_total = total - selected_value

    if not remaining_dims:
        return {selected_dim: selected_value}

    weights = {d: min_each for d in remaining_dims}
    extra_capacity = {d: max_each - min_each for d in remaining_dims}
    base_pref = {d: max(base_weights[d] - min_each, 1) for d in remaining_dims}

    remaining_points = remaining_total - len(remaining_dims) * min_each
    assigned_extra = {d: 0 for d in remaining_dims}

    while remaining_points > 0:
        eligible = [d for d in remaining_dims if assigned_extra[d] < extra_capacity[d]]
        if not eligible:
            break
        chosen = max(eligible, key=lambda d: base_pref[d] / (assigned_extra[d] + 1))
        assigned_extra[chosen] += 1
        remaining_points -= 1

    final_weights = {selected_dim: selected_value}
    for d in remaining_dims:
        final_weights[d] = min_each + assigned_extra[d]

    diff = total - sum(final_weights.values())
    if diff != 0:
        adjustable = [d for d in remaining_dims if min_each <= final_weights[d] + diff <= max_each]
        if adjustable:
            final_weights[adjustable[-1]] += diff

    return final_weights


def format_weights_text(weights_dict):
    return " · ".join([f"{DIMENSIONS[k]['label']}: {v}%" for k, v in weights_dict.items()])


def top_vars_for_dimension(row, dim_key, n=2):
    items = []
    for var, var_meta in DIMENSIONS[dim_key]["variables"].items():
        items.append(
            {
                "label": var_meta["label"],
                "score": row[f"SCORE0_{var}"],
            }
        )
    items = sorted(items, key=lambda x: x["score"], reverse=True)
    return items[:n]


def demand_summary_text(row):
    top_items = top_vars_for_dimension(row, "DEMANDA", n=2)
    score1 = top_items[0]["score"]
    score2 = top_items[1]["score"]
    level1 = classify_level(score1)
    level2 = classify_level(score2)

    if level1 == level2:
        return (
            f"Destacan {top_items[0]['label'].lower()} y {top_items[1]['label'].lower()}, "
            f"ambos con puntuación {level1}."
        )

    return (
        f"Destacan {top_items[0]['label'].lower()} y {top_items[1]['label'].lower()}, "
        f"con puntuaciones {level1} y {level2}, respectivamente."
    )


def mobility_summary_text(row):
    mov = row["SCORE0_MOVILIDAD_PROMEDIO_DIARIA"]
    est = row["SCORE0_MOV_CANTIDAD_ESTACIONES"]
    level_mov = classify_level(mov)
    level_est = classify_level(est)

    if level_mov == level_est:
        return (
            f"La movilidad promedio diaria y la cantidad de estaciones presentan "
            f"puntuaciones {classify_level_plural((mov + est) / 2)} dentro de esta dimensión."
        )

    return (
        f"La movilidad promedio diaria presenta una puntuación {level_mov}, "
        f"mientras que la cantidad de estaciones muestra una puntuación {level_est} dentro de esta dimensión."
    )


def security_summary_text(row):
    top_item = top_vars_for_dimension(row, "SEGURIDAD", n=1)[0]
    return (
        f"Lo que indica una menor exposición relativa al riesgo dentro del conjunto analizado. "
        f"El mejor desempeño relativo se observa en {top_item['label'].lower()}."
    )


def poi_summary_text(row):
    top_item = top_vars_for_dimension(row, "PTOS_INTERES", n=1)[0]
    return (
        f"El principal aporte dentro de la dimensión proviene de {top_item['label'].lower()}, "
        f"con puntuación {classify_level(top_item['score'])}."
    )


def competition_summary_text(row):
    direct = row["SCORE0_COMPETENCIA_DIRECTA_KM2"]
    indirect = row["SCORE0_COMPETENCIA_INDIRECTA_KM2"]

    better = "competencia indirecta" if indirect >= direct else "competencia directa"
    worse = "competencia directa" if indirect >= direct else "competencia indirecta"

    dim_score = row["COMPETENCIA"]

    if dim_score >= 70:
        intro = "Lo que indica una presión competitiva relativamente más moderada dentro del modelo."
    elif dim_score >= 40:
        intro = "Lo que indica una presión competitiva intermedia dentro del modelo."
    else:
        intro = "Lo que indica una presión competitiva relativamente más exigente dentro del modelo."

    return f"{intro} La dimensión muestra mejor desempeño en {better} que en {worse}."


def cost_summary_text(row):
    score = row["SCORE0_ALQ_PRECIO_PIE2_ANUAL"]

    if score >= 70:
        return "Lo que indica un nivel de alquiler relativamente más bajo dentro del conjunto analizado."
    if score >= 40:
        return "Lo que indica un nivel de alquiler intermedio dentro del conjunto analizado."
    return "Lo que indica un nivel de alquiler relativamente más alto dentro del conjunto analizado."


def dimension_summary_line(row, dim_key):
    dim_label = DIMENSIONS[dim_key]["label"]
    dim_score = row[dim_key]
    level = classify_level(dim_score)

    if dim_key == "DEMANDA":
        detail = demand_summary_text(row)
    elif dim_key == "MOVILIDAD":
        detail = mobility_summary_text(row)
    elif dim_key == "SEGURIDAD":
        detail = security_summary_text(row)
    elif dim_key == "PTOS_INTERES":
        detail = poi_summary_text(row)
    elif dim_key == "COMPETENCIA":
        detail = competition_summary_text(row)
    elif dim_key == "COSTE":
        detail = cost_summary_text(row)
    else:
        detail = ""

    return f"- **{dim_label}**: puntuación {level} ({dim_score:.1f}/100). {detail}"


def ensure_filter_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = value


def reset_filter_state(defaults):
    for k, v in defaults.items():
        st.session_state[k] = v


def get_filter_defaults(df, cluster_options):
    return {
        "filter_clusters": cluster_options,
        "filter_score_range": (
            float(df["SCORE_ESCENARIO"].min()),
            float(df["SCORE_ESCENARIO"].max()),
        ),
        "filter_rent_range": (
            float(df["ALQ_PRECIO_PIE2_ANUAL"].min()),
            float(df["ALQ_PRECIO_PIE2_ANUAL"].max()),
        ),
        "filter_competition_range": (
            float(df["COMPETENCIA_DIRECTA_KM2"].min()),
            float(df["COMPETENCIA_DIRECTA_KM2"].max()),
        ),
        "filter_mobility_range": (
            float(df["MOVILIDAD_PROMEDIO_DIARIA"].min()),
            float(df["MOVILIDAD_PROMEDIO_DIARIA"].max()),
        ),
        "filter_zones": sorted(df["NOMBRE_ZONA"].dropna().unique().tolist()),
    }


def initialize_weight_state(state_key, defaults):
    if state_key not in st.session_state:
        st.session_state[state_key] = defaults.copy()


# =========================================================
# CARGA Y PREPARACIÓN
# =========================================================
st.title("TFM GRUPO 7 SITE SELECTION MANHATTAN")
st.caption("Aplicación interactiva para scoring multicriterio, escenarios de decisión y análisis territorial.")

try:
    raw_df, micro_df, macro_df, consolidado_df, geojson = load_data()
    df = prepare_dataframe(raw_df, micro_df, macro_df, consolidado_df)
except Exception as e:
    st.error(str(e))
    st.stop()

missing_cols = validate_columns(df)
if missing_cols:
    st.error(f"Faltan columnas necesarias para la aplicación: {missing_cols}")
    st.stop()

geo_field = detect_geojson_id_field(geojson)
if geo_field is None:
    st.error("No se pudo detectar el campo ID del GeoJSON.")
    st.stop()

geojson_ids = extract_geojson_ids(geojson, geo_field)
geojson_id_set = set([x for x in geojson_ids if x is not None])


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.header("Filtros y escenario")

all_cluster_options = sorted([c for c in df["CLUSTER"].dropna().unique().tolist()])
ensure_filter_state("filter_clusters", all_cluster_options)

selected_clusters = st.sidebar.multiselect(
    "Cluster",
    options=all_cluster_options,
    default=st.session_state["filter_clusters"],
    format_func=lambda x: CLUSTER_LABELS.get(int(x), f"Cluster {x}"),
    key="filter_clusters",
)

scenario_name = st.sidebar.selectbox(
    "Escenario de decisión",
    options=list(SCENARIOS.keys()),
)

scenario = SCENARIOS[scenario_name]

default_weights_text = format_weights_text(scenario["weights"])
st.sidebar.markdown(
    f"""
    <div class="scenario-box">
        <strong>{scenario_name}</strong><br>
        {scenario["description"]}
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div class="note-box">
        <strong>Pesos por defecto del escenario</strong><br>
        {default_weights_text}<br><br>
        <strong>Nota de interacción:</strong> las dimensiones principales concentran el 60% del peso total
        y las dimensiones de contexto el 40%. Puedes modificar los pesos dentro de cada bloque,
        y la aplicación reajusta automáticamente las demás dimensiones para conservar esta lógica.
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("### Ajuste de pesos")

# PRINCIPALES
st.sidebar.markdown("**Dimensiones principales**")
main_dims = scenario["main_dims"]
main_defaults = {d: scenario["weights"][d] for d in main_dims}
main_weights_key = f"main_weights_{scenario_name}"
initialize_weight_state(main_weights_key, main_defaults)

main_min = 16
main_max = 60

main_selected = st.sidebar.selectbox(
    "Dimensión principal a modificar",
    options=main_dims,
    format_func=lambda x: DIMENSIONS[x]["label"],
    key=f"main_selected_{scenario_name}",
)

main_lower, main_upper = compute_feasible_bounds(
    total=60,
    dims_count=len(main_dims),
    min_each=main_min,
    max_each=main_max,
)

current_main_weights = st.session_state[main_weights_key].copy()
main_current_value = int(current_main_weights[main_selected])
main_current_value = max(main_lower, min(main_current_value, main_upper))

main_selected_value = st.sidebar.slider(
    f"Peso de {DIMENSIONS[main_selected]['label']} (%)",
    min_value=main_lower,
    max_value=main_upper,
    value=main_current_value,
    step=1,
)

if main_selected_value != current_main_weights[main_selected]:
    st.session_state[main_weights_key] = allocate_remaining(
        selected_dim=main_selected,
        selected_value=main_selected_value,
        dims=main_dims,
        total=60,
        min_each=main_min,
        max_each=main_max,
        base_weights=current_main_weights,
    )

current_main_weights = st.session_state[main_weights_key]
for d in main_dims:
    if d != main_selected:
        st.sidebar.info(f"{DIMENSIONS[d]['label']}: {current_main_weights[d]}% (ajuste automático)")

# CONTEXTO
st.sidebar.markdown("**Dimensiones de contexto**")
context_dims = scenario["context_dims"]
context_defaults = {d: scenario["weights"][d] for d in context_dims}
context_weights_key = f"context_weights_{scenario_name}"
initialize_weight_state(context_weights_key, context_defaults)

context_min = 5
context_max = 15

context_selected = st.sidebar.selectbox(
    "Dimensión de contexto a modificar",
    options=context_dims,
    format_func=lambda x: DIMENSIONS[x]["label"],
    key=f"context_selected_{scenario_name}",
)

context_lower, context_upper = compute_feasible_bounds(
    total=40,
    dims_count=len(context_dims),
    min_each=context_min,
    max_each=context_max,
)

current_context_weights = st.session_state[context_weights_key].copy()
context_current_value = int(current_context_weights[context_selected])
context_current_value = max(context_lower, min(context_current_value, context_upper))

context_selected_value = st.sidebar.slider(
    f"Peso de {DIMENSIONS[context_selected]['label']} (%)",
    min_value=context_lower,
    max_value=context_upper,
    value=context_current_value,
    step=1,
)

if context_selected_value != current_context_weights[context_selected]:
    st.session_state[context_weights_key] = allocate_remaining(
        selected_dim=context_selected,
        selected_value=context_selected_value,
        dims=context_dims,
        total=40,
        min_each=context_min,
        max_each=context_max,
        base_weights=current_context_weights,
    )

current_context_weights = st.session_state[context_weights_key]
for d in context_dims:
    if d != context_selected:
        st.sidebar.info(f"{DIMENSIONS[d]['label']}: {current_context_weights[d]}% (ajuste automático)")

effective_weights = {**st.session_state[main_weights_key], **st.session_state[context_weights_key]}
scenario_scored = compute_scenario_scores(df, effective_weights)

# FILTROS
st.sidebar.markdown("### Filtros adicionales")

filter_defaults = get_filter_defaults(scenario_scored, all_cluster_options)
ensure_filter_state("filter_score_range", filter_defaults["filter_score_range"])
ensure_filter_state("filter_rent_range", filter_defaults["filter_rent_range"])
ensure_filter_state("filter_competition_range", filter_defaults["filter_competition_range"])
ensure_filter_state("filter_mobility_range", filter_defaults["filter_mobility_range"])
ensure_filter_state("filter_zones", filter_defaults["filter_zones"])

if st.sidebar.button("Restablecer filtros", use_container_width=True):
    reset_filter_state(filter_defaults)
    st.rerun()

score_range = st.sidebar.slider(
    "Score del escenario (0–100)",
    min_value=0.0,
    max_value=100.0,
    value=st.session_state["filter_score_range"],
    key="filter_score_range",
)

rent_range = st.sidebar.slider(
    "Alquiler (USD/pie²/año)",
    min_value=float(scenario_scored["ALQ_PRECIO_PIE2_ANUAL"].min()),
    max_value=float(scenario_scored["ALQ_PRECIO_PIE2_ANUAL"].max()),
    value=st.session_state["filter_rent_range"],
    key="filter_rent_range",
)

competition_range = st.sidebar.slider(
    "Competencia directa (competidores/km²)",
    min_value=float(scenario_scored["COMPETENCIA_DIRECTA_KM2"].min()),
    max_value=float(scenario_scored["COMPETENCIA_DIRECTA_KM2"].max()),
    value=st.session_state["filter_competition_range"],
    key="filter_competition_range",
)

mobility_range = st.sidebar.slider(
    "Movilidad promedio diaria",
    min_value=float(scenario_scored["MOVILIDAD_PROMEDIO_DIARIA"].min()),
    max_value=float(scenario_scored["MOVILIDAD_PROMEDIO_DIARIA"].max()),
    value=st.session_state["filter_mobility_range"],
    key="filter_mobility_range",
)

zone_options = sorted(scenario_scored["NOMBRE_ZONA"].dropna().unique().tolist())
selected_zones = st.sidebar.multiselect(
    "Zonas",
    options=zone_options,
    default=st.session_state["filter_zones"],
    key="filter_zones",
)


# =========================================================
# APLICACIÓN DE FILTROS
# =========================================================
filtered = scenario_scored.copy()

if selected_clusters:
    filtered = filtered[filtered["CLUSTER"].isin(selected_clusters)].copy()
else:
    filtered = filtered.iloc[0:0].copy()

filtered = filtered[
    filtered["SCORE_ESCENARIO"].between(score_range[0], score_range[1]) &
    filtered["ALQ_PRECIO_PIE2_ANUAL"].between(rent_range[0], rent_range[1]) &
    filtered["COMPETENCIA_DIRECTA_KM2"].between(competition_range[0], competition_range[1]) &
    filtered["MOVILIDAD_PROMEDIO_DIARIA"].between(mobility_range[0], mobility_range[1])
].copy()

if selected_zones:
    filtered = filtered[filtered["NOMBRE_ZONA"].isin(selected_zones)].copy()
else:
    filtered = filtered.iloc[0:0].copy()

filtered = filtered.sort_values(["SCORE_ESCENARIO", "VARIABILIDAD_ENTRE_ESCENARIOS"], ascending=[False, True])

if filtered.empty:
    st.warning("No hay zonas que cumplan con la combinación actual de escenario, pesos y filtros.")
    st.stop()

best_zone = filtered.iloc[0]
top_subdims = get_top_subdimensions(best_zone, top_n=3)
top_subdim_text = " · ".join([f"{x['label']} ({fmt_num(x['contrib'], 1)})" for x in top_subdims])


# =========================================================
# RESUMEN DE FILTROS ACTIVOS
# =========================================================
st.markdown("### Filtros activos")
st.caption("Resumen del escenario, los pesos efectivos y las restricciones actualmente aplicadas al análisis.")

excluded_clusters = [CLUSTER_LABELS[c] for c in all_cluster_options if c not in selected_clusters]
excluded_clusters_text = ", ".join(excluded_clusters) if excluded_clusters else "ninguno"

chips = [
    f"Escenario: {scenario_name}",
    f"Score mínimo: {fmt_num(score_range[0], 0)}",
    f"Renta máxima: {fmt_num(rent_range[1], 2)}",
    f"Competencia directa máxima: {fmt_num(competition_range[1], 2)}",
    f"Clusters excluidos: {excluded_clusters_text}",
    f"{len(filtered)} zonas visibles",
]
render_chips(chips)

st.markdown(
    f"""
    <div class="note-box">
        <strong>Pesos efectivos aplicados</strong><br>
        {format_weights_text(effective_weights)}
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# KPIS
# =========================================================
c1, c2, c3, c4, c5 = st.columns([2.0, 1.2, 1.0, 1.5, 1.4])

with c1:
    metric_card(
        "Mejor zona",
        best_zone["NOMBRE_ZONA"],
        f"ID: {best_zone['ID_ZONA']}",
    )

with c2:
    metric_card(
        "Score del escenario",
        f"{best_zone['SCORE_ESCENARIO']:.2f}",
        scenario_name,
    )

with c3:
    metric_card(
        "Zonas visibles",
        f"{len(filtered)}",
        "Tras aplicar filtros",
    )

with c4:
    metric_card(
        "Ranking global",
        fmt_int(best_zone["RANKING_GLOBAL"]),
        best_zone["CONSISTENCIA_ESCENARIOS"],
    )

with c5:
    metric_card(
        "Subdimensiones dominantes",
        top_subdim_text,
        "Top 3 variables con mayor aporte",
    )


# =========================================================
# TABS
# =========================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🗺️ Mapa", "🏆 Ranking", "📊 Gráficos", "📘 Metodología", "⚠️ Limitaciones del modelo"]
)


# =========================================================
# TAB MAPA
# =========================================================
with tab1:
    st.subheader("Mapa interactivo por escenario y dimensiones")

    map_options = ["SCORE_ESCENARIO"] + list(DIMENSIONS.keys())
    option_labels = {
        "SCORE_ESCENARIO": f"Score final - {scenario_name}",
        "DEMANDA": "Censo (Demanda)",
        "MOVILIDAD": "Movilidad",
        "SEGURIDAD": "Seguridad",
        "PTOS_INTERES": "Puntos de interés",
        "COMPETENCIA": "Competencia",
        "COSTE": "Coste",
    }

    map_metric = st.selectbox(
        "Variable a visualizar en el mapa",
        options=map_options,
        format_func=lambda x: option_labels[x],
    )

    map_df = filtered.copy()
    map_df["ID_ZONA"] = map_df["ID_ZONA"].apply(clean_zone_id)
    map_df = map_df[map_df["ID_ZONA"].isin(geojson_id_set)].copy()

    if map_df.empty:
        st.error("No hay coincidencias entre los IDs filtrados y el GeoJSON.")
        st.stop()

    fig_map = px.choropleth_mapbox(
        map_df,
        geojson=geojson,
        locations="ID_ZONA",
        featureidkey=f"properties.{geo_field}",
        color=map_metric,
        hover_name="NOMBRE_ZONA",
        hover_data={
            "ID_ZONA": True,
            "CLUSTER_FILTER": True,
            "SCORE_ESCENARIO": ":.2f",
            "RANK": True,
            "DEMANDA": ":.2f",
            "MOVILIDAD": ":.2f",
            "SEGURIDAD": ":.2f",
            "PTOS_INTERES": ":.2f",
            "COMPETENCIA": ":.2f",
            "COSTE": ":.2f",
        },
        mapbox_style="carto-positron",
        center={"lat": 40.7831, "lon": -73.9712},
        zoom=10.4,
        opacity=0.78,
        color_continuous_scale="Viridis",
        range_color=(0, 100),
    )

    fig_map.update_layout(
        height=720,
        margin=dict(l=0, r=0, t=0, b=0),
        coloraxis_colorbar_title="Puntos",
    )

    st.plotly_chart(fig_map, use_container_width=True)

    summary_lines = [
        dimension_summary_line(best_zone, "DEMANDA"),
        dimension_summary_line(best_zone, "MOVILIDAD"),
        dimension_summary_line(best_zone, "SEGURIDAD"),
        dimension_summary_line(best_zone, "PTOS_INTERES"),
        dimension_summary_line(best_zone, "COMPETENCIA"),
        dimension_summary_line(best_zone, "COSTE"),
    ]

    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.markdown(f"### Descripción de la mejor zona: **{best_zone['NOMBRE_ZONA']}**")
    st.markdown(
        f"En el escenario **{scenario_name}**, esta zona obtiene un score de "
        f"**{best_zone['SCORE_ESCENARIO']:.2f}/100** con la distribución actual de pesos."
    )
    st.markdown("**Resumen por dimensiones**")
    st.markdown("\n".join(summary_lines))
    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# TAB RANKING
# =========================================================
with tab2:
    st.subheader("Top 10 zonas según filtros")

    st.markdown('<div class="group-title">Contexto</div>', unsafe_allow_html=True)
    render_html_table(build_grouped_context(filtered, scenario_name))

    st.markdown('<div class="group-title">Dimensiones</div>', unsafe_allow_html=True)
    render_html_table(build_grouped_dimensions(filtered))

    st.markdown('<div class="group-title">Subdimensiones (valores originales)</div>', unsafe_allow_html=True)
    render_html_table_multiindex(build_grouped_subdimensions(filtered))

    csv_download = filtered.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="⬇️ Descargar ranking filtrado",
        data=csv_download,
        file_name="ranking_site_selection_manhattan.csv",
        mime="text/csv",
    )


# =========================================================
# TAB GRÁFICOS
# =========================================================
with tab3:
    st.subheader("Gráficos de apoyo a la decisión")

    top10_chart = filtered.head(10).copy()
    top10_chart["score_txt"] = top10_chart["SCORE_ESCENARIO"].round(1)

    fig_bar = px.bar(
        top10_chart.sort_values("SCORE_ESCENARIO", ascending=True),
        x="SCORE_ESCENARIO",
        y="NOMBRE_ZONA",
        orientation="h",
        text="score_txt",
        color="CLUSTER_FILTER",
        labels={
            "SCORE_ESCENARIO": "Score del escenario",
            "NOMBRE_ZONA": "Zona",
            "CLUSTER_FILTER": "Cluster",
        },
    )
    fig_bar.update_traces(textposition="outside")
    fig_bar.update_layout(height=520, margin=dict(l=0, r=20, t=10, b=0))
    st.plotly_chart(fig_bar, use_container_width=True)

    compare_top = filtered.head(5).copy()
    compare_dims = compare_top[["NOMBRE_ZONA", "DEMANDA", "MOVILIDAD", "SEGURIDAD", "PTOS_INTERES", "COMPETENCIA", "COSTE"]]
    compare_dims = compare_dims.melt(id_vars="NOMBRE_ZONA", var_name="Dimension", value_name="Score")
    compare_dims["Dimension"] = compare_dims["Dimension"].map({
        "DEMANDA": "Demanda",
        "MOVILIDAD": "Movilidad",
        "SEGURIDAD": "Seguridad",
        "PTOS_INTERES": "Puntos de interés",
        "COMPETENCIA": "Competencia",
        "COSTE": "Coste",
    })

    fig_compare = px.bar(
        compare_dims,
        x="Dimension",
        y="Score",
        color="NOMBRE_ZONA",
        barmode="group",
        labels={"Score": "Puntuación", "NOMBRE_ZONA": "Zona"},
    )
    fig_compare.update_layout(height=520, margin=dict(l=0, r=20, t=10, b=0))
    st.plotly_chart(fig_compare, use_container_width=True)

    consistency_chart = filtered.head(10).copy()
    fig_cons = px.scatter(
        consistency_chart,
        x="VARIABILIDAD_ENTRE_ESCENARIOS",
        y="SCORE_ESCENARIO",
        size="RANKING_GLOBAL",
        color="CLUSTER_FILTER",
        hover_name="NOMBRE_ZONA",
        labels={
            "VARIABILIDAD_ENTRE_ESCENARIOS": "Variabilidad entre escenarios",
            "SCORE_ESCENARIO": "Score del escenario",
            "CLUSTER_FILTER": "Cluster",
        },
    )
    fig_cons.update_layout(height=520, margin=dict(l=0, r=20, t=10, b=0))
    st.plotly_chart(fig_cons, use_container_width=True)


# =========================================================
# TAB METODOLOGÍA
# =========================================================
with tab4:
    st.subheader("Metodología implementada")

    st.markdown("### Fuentes utilizadas por la aplicación")
    st.markdown(
        "- **Clusterización**: se carga desde el resultado final seleccionado del repositorio "
        f"(`{WARD_PATH.relative_to(REPO_ROOT)}`), sin recalcular clusters dentro de la aplicación.\n"
        "- **Scoring micro**: se carga desde `resultados/05_scoring/scoring_micro.csv`.\n"
        "- **Scoring macro**: se carga desde `resultados/05_scoring/scoring_macro.csv`.\n"
        "- **Escenarios consolidados**: se cargan desde `resultados/06_escenarios/consolidado_escenarios.csv`.\n"
        "- **Cartografía**: se carga desde `datos/crudos/zonas/`."
    )

    st.markdown("### Lógica del scoring")
    st.markdown(
        "La aplicación no recalcula la clusterización ni el scoring micro/macro base. "
        "Las puntuaciones por dimensión y subdimensión se toman de los resultados ya generados en el repositorio. "
        "A partir de ellos, la interacción del usuario modifica únicamente la ponderación de las dimensiones en el nivel de escenario."
    )

    st.markdown("### Pesos locales por dimensión")
    local_rows = []
    for dim_key, dim_meta in DIMENSIONS.items():
        for var, var_meta in dim_meta["variables"].items():
            local_rows.append({
                "Dimensión": dim_meta["label"],
                "Variable": var_meta["label"],
                "Peso local (%)": var_meta["weight"],
            })
    render_html_table(pd.DataFrame(local_rows))

    st.markdown("### Escenario seleccionado")
    st.markdown(
        f"**Escenario activo:** {scenario_name}\n\n"
        f"**Pesos por defecto:** {format_weights_text(scenario['weights'])}\n\n"
        f"**Pesos efectivos actuales:** {format_weights_text(effective_weights)}"
    )

    st.markdown("### Lectura del gráfico de clusters")
    cluster_info = (
        df[["CLUSTER", "CLUSTER_FILTER", "CLUSTER_DESC"]]
        .drop_duplicates()
        .sort_values("CLUSTER")
        .rename(columns={
            "CLUSTER": "ID cluster",
            "CLUSTER_FILTER": "Etiqueta",
            "CLUSTER_DESC": "Descripción",
        })
    )
    render_html_table(cluster_info)


# =========================================================
# TAB LIMITACIONES
# =========================================================
with tab5:
    st.subheader("Limitaciones del modelo")
    st.markdown(
        """
        - La aplicación depende de los resultados ya generados en el repositorio; por tanto, no sustituye el pipeline analítico original.
        - La clusterización mostrada corresponde al resultado final seleccionado (**Ward.D k = 4**) y no se recalcula en tiempo real.
        - Las modificaciones interactivas afectan únicamente a los pesos de escenario; los pesos locales de las subvariables permanecen fijos.
        - Los resultados dependen de la calidad y actualidad de las fuentes utilizadas para construir el dataset maestro.
        - La interpretación territorial debe complementarse con criterios cualitativos y conocimiento del negocio antes de una decisión final de implantación.
        """
    )
