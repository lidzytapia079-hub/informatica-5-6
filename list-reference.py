def main():
    #len()contar cuantos hay en una lista
    mylist=["pencil","computer","shirt","phone","paper"]
    print(len(mylist))

    #.append()agregar algo al final de la lista
    fruits=["apple","orange","grapes"]
    fruits.append("banana")
    print(fruits)

    #insert()especificas lo que quieres agregar a una lista y en que posicion
    fruits1=["apple","orange","grape"]
    fruits1.insert(2,"banana")
    print(fruits1)


     #sort acomodar alfabeticamente o de mayor a menor

    numbers = [1, 4, 5, 7, 9, 3,]
    numbers.sort()
    print(numbers)

    items =["lettuce","tomato", "bread", "jam", "mayonaise"]
    items.sort()
    print(items)

    numbers1=[1,4,5,7,9,3]
    numbers1.sort(reverse=True)#invierte en lugar de 0-9 ahora va de 9-0 az-za
    print(numbers1)


    #1max ,2min ,3sum - 1mas grande ,2mas chico ,3suma de todos los numeros

    numbers= [1,2,3,4,5,6,7,8,9,10,11]
    resultm = max(numbers)
    print(resultm)
    results = sum(numbers)
    print(results)
    resultsmin = min(numbers)
    print(resultsmin)

    #pop
    lista=["rojo","amarillo","verde"]
    print("lista":lista)
    lista.pop(1)removes by assigned value
    print("con pop :",lista)

    
    #remove
    lista.remove("rojo")
    print("lista con remove: ",lista)










if __name__=="__main__":
    main()
