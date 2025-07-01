from mongodb_client import conectar_mongo
from generador_eventos import generar_eventos_simulados
from evaluador import ejecutar_evaluacion
from config import N_EVENTOS
from exportador_csv import exportar_eventos_a_csv



def main():
    print("🔗 Conectando a MongoDB...")
    db = conectar_mongo()

    print("🔄 Generando eventos simulados...")
    eventos = generar_eventos_simulados(N_EVENTOS)
    db.eventos.drop()
    db.eventos.insert_many(eventos)

    print("🧪 Iniciando evaluación automatizada...")
    ejecutar_evaluacion()
    exportar_eventos_a_csv()
   

if __name__ == "__main__":
    main()
