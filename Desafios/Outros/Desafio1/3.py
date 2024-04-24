
def recomendar_plano(consumo):
  
  if consumo > 0 and consumo <= 10:
    
    return "Plano Essencial Fibra - 50Mbps"
    
  elif consumo > 10 and consumo <= 20:
    
    return "Plano Prata Fibra - 100Mbps"
    
  elif consumo > 20:
    
    return "Plano Premium Fibra - 300Mbps"
    
  

    
def inicializar():

    consumo = float(input())

    print(recomendar_plano(consumo))

inicializar()