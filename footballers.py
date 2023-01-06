def main():
    with open("zodiac.txt","r") as file:
        liste=[]
        for line in file:
            replaced=line.replace("/","")
            stripped=replaced.strip()
            splitted=stripped.split(" ")
            liste.append(splitted)

    with open("sportivi.txt","r") as footballers:
        my_list=[]
        for element in footballers:
            replaced0=element.replace("\t"," ")
            replaced1=replaced0.replace("/","")
            stripped1=replaced1.strip()
            splitted1=stripped1.split(" ")
            my_list.append(splitted1)

        for karakter in range(len(my_list)):
            for eleman in range(len(liste)):
                if (int(my_list[karakter][-1][2:4]))==int(liste[eleman][1][2:]):
                    if (int(my_list[karakter][-1][0:2]))>=int(liste[eleman][1][0:2]):
                        liste[eleman].append(f"{my_list[karakter][-3]}")
                    else:
                        liste[eleman-1].append(f"{my_list[karakter][-3]}")

        t=0
        for sayi in liste:
            summ=0
            for rakam in sayi[3:]:
                summ+=int(rakam)
            liste[t].insert(0,summ)
            t+=1
        sorted_list=sorted(liste,reverse=True)

        for sonuc in range(len(liste)):
            print(f"{sorted_list[sonuc][1]} {(sorted_list[sonuc][0])} {(int(round(float(sorted_list[sonuc][0])/150,0))*'*')}")

if __name__=="__main__":
    main()
    
