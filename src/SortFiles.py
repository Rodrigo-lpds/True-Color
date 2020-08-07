#!/usr/bin/python3
# -*- coding: utf-8 -*-

#retorna uma lista que cada posição possui 3 files netcdfs, os 3 necessarios para fazer uma projeção True color, ou seja, canal 1,2 e 3 do mesmo horario 
def SortedFiles(filesList):
  sortedList = []
  Ids = []
  for files in filesList:
    Id = (files[files.find("_s")+2:files.find("_e")])# pega apenas o tempo que começa o scam( uso esse tempo como parametro)
    if Id not in Ids:
      Ids.append(Id)
      
  
  for item in Ids:
    tupla = findFilesById(item,filesList)
    if tupla[1] == 3:
      sortedList.append(tupla[0])
      #print(tupla[0])
  return sortedList

def findFilesById(Id,fileList):
  files = []
  
  for item in fileList:
    if item.find(Id) != -1: #Caso seja encontrado o Id adiciona
      files.append(item)
  
  return files,len(files)
    