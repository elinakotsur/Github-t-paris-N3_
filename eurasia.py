class MurderStatsManager:
    def __init__(self):
        self.data = {
    "Europe":{
        "Estonia":{
            "Tallinn":{
                "murders":[5]
                }
            }
        },
    "Europe2":{
        "Finland":{
            "Helsinki":{
                "murders":[3]
                }
            }
        },
    "Asia":{
        "Japan":{
            "Tokyo":{
                "murders":[8]
                }
            }
        },
    "Afrika":{
        "Algeria":{
            "Kairo":{
                "murders":[20]
                }
            }
        }
    }
    
        
    
    def add_data(self, continent, country, city, count):
        keys = self.data[continent][ country][city]
        current =self.data
        
        for key in keys:
            if "murders" not in current:
                current["murders"]=[]
                current["murders"].append(count)
                
        
        
    
    def get_stats(self):
        return self.data
        
    
    def get_city_stats(self, continent, country, city):
        return self.data[continent][country][city]["murders"]
    
    def remove_city(self, continent, country, city):
        delete = self.data[continent][country].pop(city)
        print("deleted city", delete)
    
    
    

manager=MurderStatsManager()
manager.add_data( "Europe","Estonia","Tallinn",3)

print(manager.get_stats())
print(manager.get_city_stats("Europe", "Estonia","Tallinn"))
manager.remove_city("Europe", "Estonia","Tallinn")
print(manager.get_city_stats("Afrika", "Algeria","Kairo"))

