from src.db.mongodb import ConnectionMongo

class repository:

    def criar_documento(documento):
     
        result = ConnectionMongo.collection.insert_one(documento)
        print(f"Documento criado com o ID: {result.inserted_id}")
    
    def excluir_documento(filtro):
        
        ConnectionMongo.collection.delete_one(filtro)
        print(f"Documento excluido")
    
    def ler_documentos(filtro):
        
        repo = []

        documentos = ConnectionMongo.collection.find(filtro)
        
        for documento in documentos:

            repo.append(documento)
        
        return repo
            