val df = spark.read.option("header","true").csv("/home/dk/bdonode/data/nodelist.csv");

df.select("id").map(f => Integer.parseInt(f.getString(0))).collect.toArray


