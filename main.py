from  CollectData import CollectData
from SaveData import SaveData

collect_data = CollectData()
collect_data.collect_info()
collect_data.get_data()

save_data = SaveData()
save_data.save(collect_data.data)

