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


class Evaluacion:
    def __init__(self, nota: int, asignatura:Asignatura):
        self.__nota:int = nota
        self.__asignatura: Asignatura = asignatura

    @property
    def mostrarNota(self):
        return self.__nota

    @property
    def mostrarAsignatura(self):
        return self.__asignatura

    @classmethod
    def obtenerEvaluacion(self,nota):
        self.__nota = nota


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


class Administrativo(Usuario):
    def __init__(self,nombre:str, rut:str, correo:str):
        super().__init__(nombre=nombre,rut=rut,correo=correo)

    @property
    def _mostrarPerfil(self):
        return {'Nombre':self._nombre,'RUT':self._rut,'Correo': self._correo}
    
    @classmethod
    def generarReportes(self):
        return self
    
    @classmethod
    def gestionarMatricula(self,id):
        return self
    
    
class Estudiante(Usuario):
    def __init__(self,asignaturas:list[Asignatura],nombre:str, rut:str, correo:str):
        super().__init__(nombre=nombre,rut=rut,correo=correo)
        self.__asignaturas:list[Asignatura] = asignaturas
        self.__evaluaciones: list[Evaluacion] = []
        
    @property
    def _mostrarPerfil(self):
        return {'Nombre':self._nombre,'RUT':self._rut,'Correo': self._correo}
    
    @classmethod
    def inscribirAsignatura(self,id):
        return id
    
    def recibirEvaluacion(self,evaluacion:Evaluacion):
        print(f'{self._rut} ha recibido una evaluación del ramo {evaluacion.mostrarAsignatura} con nota {evaluacion.mostrarNota}')
        self.__evaluaciones.append(evaluacion)
    

class Docente(Usuario):
    def __init__(self,asignaturas:list[Asignatura],nombre:str, rut:str, correo:str):
        super().__init__(nombre=nombre,rut=rut,correo=correo)
        self.__asignaturas:list[Asignatura] = asignaturas
    
    @property
    def _mostrarPerfil(self):
        return {'Nombre':self._nombre,'RUT':self._rut,'Correo': self._correo}
    
    @classmethod
    def dictarAsignatura(self,id):
        return id

    @classmethod
    def evaluarAlumno(self, alumno: Estudiante, nota, asignatura):
        evaluacion = Evaluacion(nota,asignatura)
        alumno.recibirEvaluacion(evaluacion)

