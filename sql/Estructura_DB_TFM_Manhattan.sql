-- ESTRUCTURA DE BASE DE DATOS TFM SITE SELECTION MANHATTAN

-- 1. Creación de la base de datos del proyecto
CREATE DATABASE TFM_SiteSelection_Manhattan;
USE TFM_SiteSelection_Manhattan;

-- 2. Creación de la Entidad Maestra: ZONAS
CREATE TABLE ZONAS (
    ID_ZONA VARCHAR(10) NOT NULL,
    NOMBRE_ZONA VARCHAR(60) NOT NULL,
    NOMBRE_DISTRITO VARCHAR(30) NOT NULL,
    AREA_KM2 DECIMAL(10,4) NOT NULL,
    PRIMARY KEY (ID_ZONA)
);

-- 3. Creación de la Dimensión 1:1 - CENSO
-- Vinculación de las variables únicas sociodemográficas
CREATE TABLE CENSO (
    ID_ZONA VARCHAR(10) NOT NULL,
    POBLACION_TOTAL INT NOT NULL,
    EDAD_MEDIANA DECIMAL(5,2) NOT NULL,
    TASA_OCUPACION DECIMAL(5,2) NOT NULL,
    INGRESO_MEDIO_HOGAR DECIMAL(12,2) NOT NULL,
    TASA_EMPLEO DECIMAL(5,2) NOT NULL,
    TAMANO_HOGAR_PROMEDIO DECIMAL(4,2) NOT NULL,
    POBLACION_HISPANA INT NOT NULL,
    PRIMARY KEY (ID_ZONA),
    CONSTRAINT FK_CENSO_ZONAS FOREIGN KEY (ID_ZONA) REFERENCES ZONAS(ID_ZONA)
);

-- 4. Creación de la Dimensión 1:1 - COSTO_ALQUILER
-- Vinculación de las variables únicas del costo de alquiler por zona
CREATE TABLE COSTO_ALQUILER (
    ID_ZONA VARCHAR(10) NOT NULL,
    PRECIO_SQTF_ANUAL DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (ID_ZONA),
    CONSTRAINT FK_ALQUILER_ZONAS FOREIGN KEY (ID_ZONA) REFERENCES ZONAS(ID_ZONA)
);

-- 5. Creación de la Dimensión 1:N - MOVILIDAD (PK Compuesta)
-- Implementacion PK compuesta (ID_ZONA, TIPO_DIA) para garantizar registros únicos de movilidad por zona
CREATE TABLE MOVILIDAD (
    ID_ZONA VARCHAR(10) NOT NULL,
    TIPO_DIA VARCHAR(15) NOT NULL,
    VOLUMEN_TOTAL_PASAJEROS INT NOT NULL,
    CANTIDAD_ESTACIONES INT NOT NULL,
    CONSTRAINT PK_MOVILIDAD PRIMARY KEY (ID_ZONA, TIPO_DIA),
    CONSTRAINT FK_MOVILIDAD_ZONAS FOREIGN KEY (ID_ZONA) REFERENCES ZONAS(ID_ZONA)
);

-- 6. Creación de la Dimensión 1:N - SEGURIDAD (PK Compuesta)
-- Implementacion PK compuesta (ID_ZONA, TIPO_DELITO,LUGAR_DELITO) para garantizar registros únicos de incidente por zona
CREATE TABLE SEGURIDAD (
    ID_ZONA VARCHAR(10) NOT NULL,
    TIPO_DELITO VARCHAR(30) NOT NULL,
    LUGAR_DELITO VARCHAR(20) NOT NULL,
    CANTIDAD_INCIDENTES INT NOT NULL,
    CONSTRAINT PK_SEGURIDAD PRIMARY KEY (ID_ZONA, TIPO_DELITO, LUGAR_DELITO),
    CONSTRAINT FK_SEGURIDAD_ZONAS FOREIGN KEY (ID_ZONA) REFERENCES ZONAS(ID_ZONA)
);

-- 7. Creación de la Dimensión 1:N - RESTAURANTES (PK Compuesta)
-- Implementacion PK compuesta (ID_ZONA, TIPO_COCINA, CLASIFICACION_COMPETENCIA) para garantizar registros únicos de la competencia por zona
CREATE TABLE RESTAURANTES (
    ID_ZONA VARCHAR(10) NOT NULL,
    TIPO_COCINA VARCHAR(20) NOT NULL,
    CANTIDAD_LOCALES INT NOT NULL,
    CLASIFICACION_COMPETENCIA VARCHAR(20) NOT NULL,
    CONSTRAINT PK_RESTAURANTES PRIMARY KEY (ID_ZONA, TIPO_COCINA, CLASIFICACION_COMPETENCIA),
    CONSTRAINT FK_REST_ZONAS FOREIGN KEY (ID_ZONA) REFERENCES ZONAS(ID_ZONA)
);

-- 8. Creación de la Dimensión 1:N - LUGARES_INTERES (PK Compuesta)
-- Implementacion PK compuesta (ID_ZONA, CATEGORIA_LUGAR) para garantizar registros únicos de categorias de lugares de interes por zona
CREATE TABLE LUGARES_INTERES (
    ID_ZONA VARCHAR(10) NOT NULL,
    CATEGORIA_LUGAR VARCHAR(30) NOT NULL,
    CANTIDAD_LUGARES INT NOT NULL,
    CONSTRAINT PK_LUGARES_INTERES PRIMARY KEY (ID_ZONA, CATEGORIA_LUGAR),
    CONSTRAINT FK_LUGARES_ZONAS FOREIGN KEY (ID_ZONA) REFERENCES ZONAS(ID_ZONA)
);


/* --- VERIFICACIONES DE IMPORATCIONES DE LAS TABLAS --- */

SELECT * FROM ZONAS; -- Visualización de todos los datos de la tabla maestra ZONAS
SELECT COUNT(*) AS Total_Registros FROM ZONAS; -- Cantidad de regsitros en la tabla maestra ZONAS

SELECT * FROM CENSO; -- Visualización de todos los datos de la tabla CENSO
SELECT COUNT(*) AS Total_Registros FROM CENSO; -- Cantidad de regsitros en la tabla CENSO
    
SELECT * FROM COSTO_ALQUILER; -- Visualización de todos los datos de la tabla COSTO_ALQUILER
SELECT COUNT(*) AS Total_Registros FROM COSTO_ALQUILER; -- Cantidad de registros en la tabla COSTO_ALQUILER
    
SELECT * FROM MOVILIDAD; -- Visualización de todos los datos de la tabla MOVILIDAD
SELECT COUNT(*) AS Total_Registros FROM MOVILIDAD; -- Cantidad de registros en la tabla MOVILIDAD

SELECT * FROM SEGURIDAD; -- Visualización de todos los datos de la tabla SEGURIDAD
SELECT COUNT(*) AS Total_Registros FROM SEGURIDAD; -- Cantidad de registros en la tabla SEGURIDAD
    
SELECT * FROM RESTAURANTES; -- Visualización de todos los datos de la tabla RESTAURANTES
SELECT COUNT(*) AS Total_Registros FROM RESTAURANTES; -- Cantidad de registros en la tabla RESTAURANTES
    
SELECT * FROM LUGARES_INTERES; -- Visualización de todos los datos de la tabla LUGARES_INTERES
SELECT COUNT(*) AS Total_Registros FROM LUGARES_INTERES; -- Cantidad de registros en la tabla LUGARES_INTERES

