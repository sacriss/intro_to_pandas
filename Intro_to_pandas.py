#Crear un dataframe desde una lista
import pandas as pd
def createDataFrame(student_data: List[List[int]]) -> pd.DataFrame:
    # Definir nombres de columnas
    column_names = ['Nombre', 'Edad']
    
    # Crear dataframe con los datos
    df = pd.DataFrame(student_data, columns=column_names)
    
    return df

#Obtener el tamaño del dataframe
def getDataframeSize(student_data: pd.DataFrame) -> List:
    #Esta linea define una funcion llamada getDataframeSize que recibe un dataframe como argumento y devuelve una lista con el numero de filas y columnas
    return [student_data.shape[0], student_data.shape[1]]
    #El atributo 'shape' devuelve una tupla con (nº filas, nº columnas)
    #shape[0] es el numero de filas
    #shape[1] es el numero de columnas

#Mostrar las primeras tres filas del dataframe
def selectFirstThreeRows(student_data: pd.DataFrame) -> pd.DataFrame:
    return student_data.head(3)
    #El atributo 'head' devuelve las primeras n filas del dataframe
    #Si no se especifica n, devuelve las primeras 5 filas


#Ordenar el dataframe por edad de mayor a menor
def sortDataFrameByAge(student_data: pd.DataFrame) -> pd.DataFrame:
    return student_data.sort_values('Edad', ascending=False)
    #El atributo 'sort_values' ordena el dataframe segun el valor de una columna
    #Si 'ascending=False', el dataframe se ordena de mayor a menor

#Filtrar el dataframe para obtener aquellos estudiantes con edad mayor a 20
def filterDataFrameByAge(student_data: pd.DataFrame) -> pd.DataFrame:
    return student_data[student_data['Edad'] > 20]
    #El operador '[...]' se utiliza para seleccionar filas y columnas en un dataframe
    #El argumento 'student_data[student_data['Edad'] > 20]' selecciona las filas donde la edad sea mayor a 20

#Seleccionar datos
def selectData(student_data: pd.DataFrame) -> pd.DataFrame:
    return student_data.loc[students["student_id"] == 101, ["Nombre", "Edad"]]
    #El metodo 'loc' selecciona filas y columnas en un dataframe
    #El argumento 'students.loc[students["student_id"] == 101, ["Nombre", "Edad"]]' selecciona la fila con id 101 y las columnas Nombre y Edad

#Crear una nueva columna
def addColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["Salary"] * 2
    return employees
    #Creamos una nueva columna llamada bonus que multiplica por 2 los datos de la columna salary

    