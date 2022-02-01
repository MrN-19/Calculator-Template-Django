# Calculator-Template-Django

this is a template tag project for django to calculate in templates , enjoy it

# Get Started :

## 1 - Download Source Code
## 2 - Move Source next to your django project
## 3 - go to setting.py file and register "calculator" to you INSTALLED_APPS list
## 4 - enjoy

# For Using do like this in you template :


```bash
{% load calculator %}


Sum Two Number :
{{20|sum:"10"}} ---> Result Will be = 30

Minuse Two Number
{{20|min:"10"}} ---> Result Will be = 10

Multiple Two Number
{{20|mul:"10"}} ---> Result Will be = 200

Divide Two Number
{{20|div:"10"}} ---> Result Will be = 2

Pow Two Number
{{20|pow:"2"}} ---> Result Will be : 400

Sqrt Number
{{4|sqrt}} ---> Result Will be = 2

Sin Number 
{{30|sin}} ---> Result Will be = 0.5

Cos Number
{{60|cos}} ---> 0.5

Tan Number
{{10|tan}} ---> Result Will be = 0.17

```

