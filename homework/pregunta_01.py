"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    ruta_entrada = "files/input/solicitudes_de_credito.csv"
    ruta_salida = "files/output/solicitudes_de_credito.csv"
    if not os.path.exists("files/output"):
        os.makedirs("files/output")
    df_cre = pd.read_csv(ruta_entrada, sep=";", index_col=0)
    df_cre["sexo"] = df_cre["sexo"].str.strip().str.lower()
    df_cre["tipo_de_emprendimiento"] = df_cre["tipo_de_emprendimiento"].str.strip().str.lower()
    df_cre["idea_negocio"] = (
        df_cre["idea_negocio"]
        .str.strip().str.lower()
        .str.replace("á", "a")
        .str.replace("é", "e")
        .str.replace("í", "i")
        .str.replace("ó", "o")
        .str.replace("ú", "u")
        .str.replace(" ", "")
        .str.translate(str.maketrans("", "", "-._"))
    )
    df_cre["barrio"] = df_cre["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df_cre["comuna_ciudadano"] = df_cre["comuna_ciudadano"].astype(int)
    df_cre["fecha_de_beneficio"] = pd.to_datetime(df_cre["fecha_de_beneficio"], dayfirst=True, format="mixed")
    df_cre["monto_del_credito"] = (
        df_cre["monto_del_credito"]
        .str.strip()
        .str.strip("$")
        .str.replace(".00", "", regex=False)
        .str.replace(",", "", regex=False).astype(int)
    )
    df_cre["línea_credito"] = (
        df_cre["línea_credito"]
        .str.strip()
        .str.lower()
        .str.replace(" ", "")
        .str.translate(str.maketrans("", "", "-._"))
    )
    
    df_cre = df_cre.dropna().drop_duplicates()
    df_cre.to_csv(ruta_salida, index=False, sep=";")



pregunta_01()