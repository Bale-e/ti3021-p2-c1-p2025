class Asignatura:
    def __init__(self, id: int, nombre: str):
        self.__id:int = id
        self.__nombre:str = nombre

    @property
    def mostrarId(self):
        return {'Asignatura:':self.__nombre, 'ID': slef.__id}
    
    @property
    def mostrarNombre(self):
        return self.__nombre

    @classmethod
    def mostrarAsignatura(self):
        return { 'id': self.__id, 'nombre': self.__nombre }

#########################################################################

class Evaluacion:
    def __init__(self, nota: int, asignatura:Asignatura):
        self.__nota:int = nota
        self.__asignatura: Asignatura = asignatura

    @property
    def mostrarNota(self):
        return {'Nota': self.__nota}

    @classmethod
    def obtenerEvaluacion(self,nota):
        self.__nota = nota

##########################################################################

class Usuario:
    def __init__(self, nombre:str, rut:str, correo:str):
        self._nombre: str = nombre
        self._rut: str = rut
        self._correo: str = correo
    
    @property
    def _mostrarPerfil(self):
        return {'Nombre': self._nombre, 'RUT': self._rut, 'Correo': self._correo }
    
    @classmethod
    def nombre(self,nombre):
        self._nombre = nombre
    
    @classmethod
    def rut(self,rut:str):
        self._rut = rut

    @classmethod
    def correo(self,correo:str):
        self._corre = correo

#########################################################################

class Administrativo:
    @property
    def _mostrarPerfil(self):
        return {'Nombre':self._nombre,'RUT':self._rut,'Correo': self._correo}
    
    @classmethod
    def generarReportes(self):
        return self
    
    @classmethod
    def gestionarMatricula(self,id):
        return self
    
##########################################################################
    
class Estudiante:
    def __init__(self,asignaturas:list[Asignatura]):
        self.__asignaturas:list[Asignatura] = asignaturas
    
    @property
    def _mostrarPerfil(self):
        return {'Nombre':self._nombre,'RUT':self._rut,'Correo': self._correo}
    
    @classmethod
    def inscribirAsignatura(self,id):
        return id
    
    @classmethod
    def recibirEvaluacion(self):
        return Evaluacion
    
##########################################################################

class Docente:
    def __init__(self,asignaturas:list[Asignatura]):
        self.__asignaturas:list[Asignatura] = asignaturas

    @property
    def _mostrarPerfil(self):
        return {'Nombre':self._nombre,'RUT':self._rut,'Correo': self._correo}
    
    @classmethod
    def dictarAsignatura(self,id):
        return id

    @classmethod
    def evaluarAlumno(self,nota):
        Evaluacion.obtenerEvaluacion(self,nota)
