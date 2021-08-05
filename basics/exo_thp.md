# Exercices - TheHackingProject

La formation TheHackingProject est utilisé Ruby, mais on peut travailler avec peu n'importe quelle langage qu'on veut :)).
Ici, je vais donner la réponse en `python`

Phần nội dụng trong file này, viết hoàn toàn trực tiếp trong trong file markdown theo logic của python, các lời giải chưa kiểm tra lại kết quả, nên sẽ có những lời giải chưa chính xác hoàn toàn. Quan trọng là lấy ý tưởng của lời giải để hiểu cách làm.


### 2.1. Bonjour monde
Créé un programme exo_01.rb qui affiche “Bonjour, monde !“.
Voici les lignes qu’il doit avoir d’affichées lorsque tu l’exécutes :
`$ ruby exo_01.rb`
- **En vn**: viết một chương trình exo_01.py in ra "Bonjour, monde!"
- Résultat demandé: "Bonjour, monde!"
- Solution
```python
print("Bonjour, monde!)
```

### 2.2. Un programme qui dit bonjour
Écris un programme `exo_02.rb` qui demande le prénom de l’utilisateur, et qui salue l’utilisateur avec “Bonjour, prénom !”
- En vn: Viết chương trình exo_02.py mà khi chạy, chương trình sẽ yêu cầu người dùng nhập từ bàn phím tên của họ,
  rồi sau đó print xin chào + tên người đó ra màn hình:
- Résultat demandé: `Bonjour, <nom utilisateur>!`

- Solution
```python
name = input("Enter your name: ")
print("Bonjour" + name)
# or print(f"Bonjour {name}!")
```


### 2.3. Un programme qui calcule des âges
Écris un programme exo_03.rb qui demande son année de naissance à l’utilisateur,
puis qui ressort l’âge que l’utilisateur a eu en 2017.

- En vn: Viết chương trình `exo_03.py`, yêu cầu nhập vào năm sinh của người dùng,
  sau đó tính toán tuổi của họ vào năm 2017

- Résultat demandé:
  ex: yearInput = 1997 --> en 2017, cet utilisateur a 2017-1997 = 20 ans. Thời điểm đẹp nhất trên đời :))

- Solution
```python
yearOfBirth = int(input("Enter your year of birth: "))
ageIn2017 = 2017 - yearOfBirth
print(f"In 2017, I'am {ageIn2017} year olds")
```

### 2.4. Un programme centenaire
Écris un programme `exo_04.rb` qui demande son année de naissance à l’utilisateur,
puis qui ressort l’année où l’utilisateur aura 100 ans.

- En vn: viết một chương trình `exo_04.py` yêu cầu nhập năm sinh của người dùng,
  sau đó in ra năm mà người đó 100 tuổi
- Résultat demandé:
  ex: yearInput = 1997 --> résultat = 1997 + 100 = 2097

- Solution
```python
yearOfBirth = int(input("Enter your year of birth, please: "))
age100 = yearOfBirth + 100
print(f"The year when I'm 100 year olds is: {age100}")
```
- Résultat:
```
The year when I'm 100 year olds is: 2097
```


### 2.5. Un programme qui répète
Écris un programme `exo_05.rb` qui demande un nombre à l’utilisateur,
puis qui écrit autant de fois “Salut, ça farte ?”

- En vn: viết một chương trình `exo_05.py`, yêu cầu nhập vào một số bất kỳ, rồi in ra số lần câu "Salut, ça farte?" bằng với số vừa nhập vào đó
- Solution1: Phương pháp vòng lặp truyền thống (boucle traditionnel)
```python
number = int(input("Enter a number: "))
for num in range(number):
    print("Salut, ça farte?")
```
- Solution: "python way" - sử dụng tiện ích của python
```python
number = int(input("Enter a number: "))
print(number*"Salut, ça farte?\n")
```

Ký hiệu `\n` để chỉ định xuống dòng mới,

<số đếm> * <string> : thì python sẽ cho phép in string đó vời số lần = số đếm

- Résultat:
```bash
Salut, ça farte?
Salut, ça farte?
Salut, ça farte?
Salut, ça farte?
...

```

### 2.6. Un programme qui répète (bis)
Écris un programme exo_06.rb qui demande un nombre à un utilisateur,
puis qui écrit autant de fois -1 “Bonjour toi !“.
Ainsi, si l’utilisateur rentre 10,
le programme devra écrire 9 fois “Bonjour toi !”

- En vn: Viết một chương trình `exo_06.py`, yêu cầu nhập vào một số, sau đó in ra trừ 1 số lần câu: "Bonjour toi!"
  ex: numInput = 8 --> in ra 7 lần câu "Bonjour toi!"

numInput = 6 --> in ra 5 lần câu "Bonjour toi!"

- Solution
```python
num = int(input("Enter a random number: "))
print((num-1)*"Bonjour toi!")
```
- Résultat:
```bash
Bonjour toi!
Bonjour toi!
Bonjour toi!
Bonjour toi!
...

```
### 2.7. Compter
Écris un programme `exo_07.rb` qui demande un nombre à l’utilisateur,
puis qui compte jusqu’à ce nombre.

- En vn: viết một chương trình `exo_07.py` yêu câù nhập vào một số, sau đó in từ 1 đến số đó ra màn hình
- Solution
```python
numInput = int(input("Enter a number: ")
for num in range(numInput):
    print(num + 1)
```
- Résultat:
```
1
2
3
4
5
...
```
### 2.8. Compte à rebours
Écris un programme exo_08.rb qui demande un nombre à l’utilisateur,
puis qui affiche un compte à rebours à partir de ce nombre, jusqu’à 0.

- En vn: bài toán đếm ngược: viết chương trình `exo_08.py`, yêu cầu nhập từ bàn phím vào một số, rồi in ra màn hình từ số đó trở về 0
- Solution
```python
numInput = int(input("Enter a number: ")
print("Count down\n")
for num in range(numInput):
    print(numInput - num)
```
- Résultat:
```
...
5
4
3
2
1
0
```

### 2.9. Afficher les années
Écris un programme exo_09.rb qui demande son année de naissance à l’utilisateur,
puis qui va ressortir chaque année depuis son année de naissance jusqu’aujourd’hui.
- En vn: viết một chương trình  `exo_09.py`, nhập vào năm sinh của người dùng,
  sau đó in ra mỗi năm từ năm sinh đó đến năm nay

- Solution
````python
thisYear = 2021 # or more complexe, we can also use library date to get automatic this year
yearOfBirthDay = int(input("Enter your year of birth: "))
for year in range(yearOfBirthDay, thisYear + 1):
    print(year)
````

`Note`: Nhớ lại cách dùng của `range`: range(start, end)

- Solution 2
````python
thisYear = 2021 # or more complexe, we can also use library date to get automatic this year
yearOfBirthDay = int(input("Enter your year of birth: "))
while yearOfBirthDay <= thisYear:
    print(yearOfBirthDay)
    yearOfBirthDay += 1
````
Với cách này, thì yearOfBirthDay, sẽ tự động tăng dần đến thisYear, khi nó lớn hơn thisYear, thì vòng lặp tự lặp lại. Dịch tương tự giống tiếng viêt: trong khi <điều kiện>: thì làm điều này.

- Résultat
```bash
1997
1998
1999
2000
...
2021
```

### 2.10. Afficher tous les âges
Écris un programme exo_10.rb qui demande son année de naissance à l’utilisateur
et qui va afficher chaque année depuis son année de naissance jusqu’aujourd’hui.
Pour chaque année affichée,
le programme devra annoncer l’âge que l’utilisateur avait cette année-là.

- En vn: viết chương trình `exo_10.py`, yêu cầu nhập vào năm sinh, sau đó in ra mỗi năm từ năm đó đến nay.
  Khi in ra mỗi năm đó, cần phải đưa ra số tuổi của người dùng tại năm đó nữa.

- Solution

```python
yearOfBirth = int(print("Enter your year of birth: "))
thisYear = 2021
year = yearOfBirth
for year in range(yearOfBirthDay, thisYear + 1):
    age = year - yearOfBirth
    print(f"{year - age} year olds")

```

- Solution 2
```python
yearOfBirth = int(print("Enter your year of birth: "))
thisYear = 2021
year = yearOfBirth
while year <= thisYear:
    age = year - yearOfBirth
    print(f"{year - age} year olds")
    year += 1
    
```

- Résultat
```bash
1997 - 0 year olds
1998 - 1 year olds
1999 - 2 year olds
2000 - 3 year olds
...
2021 -  don't know
```

Note: nếu ham học hỏi hơn, thích mày mò một chút, có thể thêm điều kiện
đề viết ra khi số tuổi là 0 hoặc 1, thì chữ `year old` sẽ k có `s`. Try it =))


### 2.11. Virer les années
Le programme `exo_10.rb` est cool, mais on peut l’améliorer.
Écris un programme `exo_11.rb` qui va demander son âge à l’utilisateur,
et qui, pour chaque année depuis sa naissance, dira “Il y a X ans, tu avais Y ans”.

- En vn:  Viết chương trình `exo_11.py`, nhập vào số tuổi
  của người dùng, tại mỗi năm từ đó đến nay, tính toán số năm so với hiên tại + số tuổi với format:
  "Il y a X ans, tu avais Y ans"

- Solution
```python
age = int(input("Enter your age: ")
yearOfBirth = 2021 - age
count = 0
for year in range(yearOfBirth, 2022):
    print(f"(En {year}) Il y a {2021-year}, tu avais {count} ans")
    count += 1
```  
- Solution
```python
age = int(input("Enter your age: ")
yearOfBirth = 2021 - age
listYear = range(yearOfBirth, 2022)
for year,index in enemurate(listYear):
    print(f"(En {year}) Il y a {2021-year} ans, tu avais {index} ans")
```

- Résultat
```bash
(En 1997) Il y a 24 ans, tu avais 0 ans
(En 1998) Il y a 23 ans, tu avais 1 ans
(En 1999) Il y a 22 ans, tu avais 2 ans
...
```

### 2.12. Annoncer l’âge, option BG
Notre programme exo_11.rb est devenu beau gosse.
Écris un programme exo_12.rb qui va faire la même chose,
sauf que si X et Y sont égaux, il dira
“Il y a n ans, tu avais la moitié de l’âge que tu as aujourd’hui”.

- En vn: Tương tự như bài trên, bây h viết chương trình `exo_12.py`, nhưng cần tính toán, khi có số tuổi bằng 1 nửa hiện tại
- Solution
```python
age = int(input("Enter your age: ") # Nhớ rằng input nên luôn luôn đưa description như dạng này vào nhé. Để lúc chạy chương trình, mình hiểu là mình đang nhập cho biến gì.
yearOfBirth = 2021 - age
count = 0
halfAge = age//2 if age%2 == 0 else -1   # -1 mean, not exist haft age, ex: 21%2 !0, not exist age
for year in range(yearOfBirth, 2022):
    if halfAge > 0 and halfAge == year:
        print(f"(En {year}) Il y a {2021-year}, avais la moitié de l’âge que tu as aujourd’hui")
    else:
        print(f"(En {year}) Il y a {2021-year}, tu avais {count} ans")
    count += 1
```  

- Résultat
```bash
(En 1997) Il y a 24 ans, tu avais 0 ans
(En 1998) Il y a 23 ans, tu avais 1 ans
(En 1999) Il y a 22 ans, tu avais 2 ans
...
(En 2009) Il y a 12 ans, tu avais la moitié de l’âge que tu as aujourd’hui
...
```

### 2.13. Une liste d’email
Écris un programme exo_13.rb qui va
créer une liste de 50 faux emails et les stocker dans une array.
Voici le format que devront avoir les faux emails :
"jean.dupont.01@email.fr"
"jean.dupont.02@email.fr"
etc..

- vas-y!
- En VN: yêu cầu của đề bài là phải lưu tất cả các mail trong 1 array (list) trước, rồi sau đó mới làm gì tiếp theo thì làm
- Solutions
```
listEmail = []
for num in range(50):
  if(num < 9):
    listEmail.append(f'jean.dupont.0{num+1}@email.fr')
  else:
    listEmail.append(f'jean.dupont.{num+1}@email.fr')
    
# print to console
for email in listEmail:
  print(email)
```


### 2.14. Afficher les bons emails
Prends le programme exo_13.rb et créé un programme exo_14.rb qui va reprendre l’array des emails créés, et n’afficher que les emails avec un nombre pair.
"jean.dupont.02@email.fr"
"jean.dupont.04@email.fr"
etc..

- vas-y, essaye-le!
- En VN: như bài trên, buộc phải lưu tất cả các email vào 1 array (list) trước, rồi lặp array này, in ra email với số chẵn

```
listEmail = []
for num in range(50):
  if(num < 9):
    listEmail.append(f'jean.dupont.0{num+1}@email.fr')
  else:
    listEmail.append(f'jean.dupont.{num+1}@email.fr')
    
# print to console
count = 0
for email in listEmail:
  if(count%2 ==0):
    print(email)
```

### 2.15. La pyramide
Construis un programme exo_15.rb qui va demander à l’utilisateur un nombre entre 1 et 25 et qui va sortir une pyramide à descendre d’autant d’étages que ce nombre. Voici un exemple :
Salut, bienvenue dans ma super pyramide ! Combien d'étages veux-tu ?
5
Voici la pyramide :

```
#
##
###
####
#####
```

Je vais donner la réponse pour lui, l'autre cas, je vais te laisser de réfléchir un peu:

- Solution

```python
def pyramid1():
    num = int(input("Enter a number of start for pyramid1: "))
    for i in range(num):
        print(i*"#")

pyramid1()

```

### 2.16. La pyramide, dans l’autre sens
Reprends ton programme exo_15.rb et fais un programme pyramide.rb qui montera au lieu de descendre :
Salut, bienvenue dans ma super pyramide ! Combien d'étages veux-tu ?
5
Voici la pyramide :
```
    #
   ##
  ###
 ####
#####
```

- Trường hợp này tính toán dâú cách + số lượng dấu #
- Solutions
```python
def pyramid2():
    num = int(input("Enter a number of start for pyramid2: "))
    for i in range(num):
        print((num-i)*" " + i*"#")

pyramid2()
```

Bien que légèrement différent dans l’énoncé, ce programme est bien plus dur que le exo_15.rb, donc c’est normal de devoir réfléchir à comment le faire :sunglasses:


2.17. La pyramide, version expert
Crée un programme exo_17.rb qui va demander à l’utilisateur un nombre entre 1 et 25 et qui va sortir une pyramide qui monte et qui descend, comme montré ci-dessous :
Salut, bienvenue dans ma super pyramide ! Combien d'étages veux-tu ?
5
Voici la pyramide :
```
    #
   ###
  ##### 
 #######
#########
```

- Trường hợp này dấu cách 2 bên, và chỉ chạy cho nhừng trường hợp là số lẻ: eacNnum%2 != 0
- Solutions
```python
def pyramid3():
    num = int(input("Enter a number of start for pyramid3: "))
    for i in range(num):
        if i%2 != 0:
            space = (num-i)//2
            print(space*" " + i*"#" + space*" ")

pyramid3()
```