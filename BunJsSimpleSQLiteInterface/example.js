import { createTable, getLastId, insert, select, update, remove, setupDB } from "./main.js";

setupDB("mydb.sqlite", true);

insert("users", { name: "saluk yuzikuma"});

//update("users", "name", "Jane Doe", "name", "laba");