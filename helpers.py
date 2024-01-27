from flask import request
from data import datas
symptoms  = []
def checkSymptoms ():
    global symptoms;
    for i in range(1,19):
        if request.form.get('pilihan'+str(i)):
            symptoms.append(i)
    return symptoms   

def diagnosis():
    symptoms  = checkSymptoms()
    temp = [0 for x in range(23)]
    index = 0
    total_symptoms  = 0
    result = []
    maxSymptoms  = ["",0,[]]
    gejala = []
    
    for disease in datas.keys():
        for symptom in datas[disease].keys():
            total = 0
            for keyWeight in symptoms :
                if keyWeight in datas[disease][symptom].keys():
                    temp[index] += datas[disease][symptom][keyWeight]
                    total += datas[disease][symptom][keyWeight]
            
            temp[index] =  (temp[index]/100) * 100
            index+=1
            gejala.append(symptom + f" {round(total)}%")
    

        match disease:
            case "Keracunan Salmonellae":
                total_symptoms  = 600
            case "Keracunan Clostridium Botulinum":
                total_symptoms  = 300
            case "Keracunan Campylobacher":
                total_symptoms  = 400
            case _:
                total_symptoms  = 500
        result.append({"penyakit": disease,"nilai":(sum(temp)/total_symptoms ) * 100,"gejala":gejala})
        for r in result:
            if r['nilai'] > maxSymptoms[1]:
                maxSymptoms = [disease,r['nilai'],gejala]

        gejala = []
        temp = [0 for x in range(23)]
     
    return [result,maxSymptoms]