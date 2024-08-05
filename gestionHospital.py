class Persona:
    def __init__(self, nombre, apellido, identificacion, fecha_nacimiento):
        self._nombre = nombre
        self._apellido = apellido
        self._identificacion = identificacion
        self._fecha_nacimiento = fecha_nacimiento

    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre} {self._apellido}, Identificacion: {self._identificacion}, Fecha de nacimiento: {self._fecha_nacimiento} ")

class Paciente(Persona):
    def __init__(self, nombre, apellido, identificacion, fecha_nacimiento, historial_medico, tipo_sangre):
        super().__init__(nombre, apellido, identificacion, fecha_nacimiento)
        self._historial_medico = historial_medico
        self._tipo_sangre = tipo_sangre

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Historial médico: {self._historial_medico}, Tipo de sangre: {self._tipo_sangre}")

class Medico(Persona):
    def __init__(self, nombre, apellido, identificacion, fecha_nacimiento, especialidad, numero_licencia):
        super().__init__(nombre, apellido, identificacion, fecha_nacimiento)
        self._especialidad = especialidad
        self._numero_licencia = numero_licencia

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Especialidad: {self._especialidad}, Número de licencia: {self._numero_licencia}")

class Cita:
    def __init__(self, fecha, hora, paciente, medico):
        self._fecha = fecha
        self._hora = hora
        self._paciente = paciente
        self._medico = medico 

    def mostrar_informacion(self):
        print(f"Fecha: {self._fecha}, Hora: {self._hora}, Paciente: {self._paciente._nombre} {self._paciente._apellido}, Médico: Dr. {self._medico._nombre} {self._medico._apellido}")

class Hospital:
    def __init__(self):
        self._pacientes = []
        self._medicos = []
        self._citas = []

    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)
        print(f"se ha agregado '{paciente._nombre_apellido}' paciente. ")

    def agregar_medico(self, medico):
        self._medicos.append(medico)
        print(f"se ha agregado '{medico._nombre_apellido}'medico ")

    def programar_cita(self, fecha, hora, paciente, medico):
        nueva_cita = Cita(fecha, hora, paciente, medico)
        self._citas.append(nueva_cita)
        print(f"se ha programado una cita")

    def buscar_persona_por_nombre(self, nombre):
        for persona in self._pacientes + self._medicos:
            if persona._nombre.lower() == nombre.lower():
                persona.mostrar_informacion()

    def mostrar_informacion(paciente):
        paciente.mostrar_informacion()

paciente1 = Paciente("dante", "apellidorial", "68288574", "14-12-1999", "gastritis", "a-" )
paciente2 = Paciente ("emilia", "molina", "7399175712", "11-09-2003", "dolor de cabeza", "b+" )
medico1 = Medico ("esteban", "perez", "108828332", "10-08-2000", "general", "11111" )
medico2 = Medico ("eve", "molina", "0391331", "27-04-1999", "general", "27781938")

cita1 = Cita ("10-06-2024", "2:30 pm", "dante", "esteban")

gestion_hospital = ()

gestion_hospital.agregar_Paciente(paciente1)
gestion_hospital.agregar_paciente(paciente2)
gestion_hospital.agregar_medico(medico1)
gestion_hospital.agregar_medico(medico2)

gestion_hospital.programar_cita(cita1) 

print("lista de pacientes")
gestion_hospital.buscar_persona_por_nombre("dante")
gestion_hospital.buscar_persona_por_nombre("esteban")