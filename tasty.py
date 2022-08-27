import requests, json
#images???
def requestData(food,number):
  url = "https://tasty.p.rapidapi.com/recipes/list"
  
  querystring = {"from":"0","size":number,"tags":"under_30_minutes","q":food}
  
  headers = {
  	"X-RapidAPI-Key": "899cc56c30msh795c5c6b87c9336p1fa612jsn4f94d35687d1",
  	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers, params=querystring)
  
  data = response.json()
  #print(json.dumps(data,indent=4))
  return data


def sortRecipeData(data):
  recipelst = []
  for recipe in data["results"]:
    rec = {}
    name = recipe["name"]
    desc = recipe["description"]
    url = ""
    ingredients = []
    instructions = []
    
    #ingredients/tools
    for section in recipe["sections"]:
      for ing in section["components"]: 
        ingredients.append(ing["raw_text"])
     
    #instructions 
    for instruction in recipe["instructions"]:
      instructions.append(instruction["display_text"])
 
    #print(name,"\n",desc,"\n",url,"\n",ingredients,"\n",instructions)
    #print("\n")
    rec['name'] = name
    rec['description'] = desc
    rec['url'] = url 
    rec['ingredients'] = ingredients
    rec['instructions'] = instructions
    #print(rec)
    recipelst.append(rec)
  return recipelst

def sortText(lst):
  tlst = []
  for i  in lst:
    text = ("Title:" +"\n\n" +i['name'] + 
            "\n\n"+"Description:" +"\n\n" + i['description']
            +"\n\n"+"Ingredients:"+"\n\n")
    
    for ingredient in i['ingredients']:
      text+=ingredient+"\n"
      
    text+= "\n\n"+"Instructions"+"\n\n"
    for instructions in i['instructions']:
      text+=instructions+"\n"
    tlst.append(text)
  return tlst
#if __name__=="__main__":
#  data = requestData("pie",5)
#  info = sortRecipeData(data)
  
#ingredients/tools
#for recipe in data["results"]:
#  #print(json.dumps(recipe,indent=4))
#  for section in recipe["sections"]:
    #print(json.dumps(i,indent=4))
    #print("done")
#    for ing in section["components"]: 
#      print(ing["raw_text"])
#    print("\n")
    

