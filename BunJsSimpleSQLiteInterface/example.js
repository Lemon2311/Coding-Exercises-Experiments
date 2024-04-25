import { createTable, getLastId, insert, select, update, remove } from "./main.js";

// createTable("users", "id INTEGER PRIMARY KEY, name TEXT");

// let i = getLastId("users") || 0;

// insert("users", ++i, "Alice");

// console.log(select("users", "name", "Alice"));

// update("users", 1, "name", "Bob");

console.log(select("users", "name", "Bob"));

remove("users", select("users", "name", "Bob")[0].id);

console.log(select("users", "name", "Bob"));
