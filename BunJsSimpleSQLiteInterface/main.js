import {Database} from "bun:sqlite";

const db = new Database("mydb.sqlite", {create: true});

const insert = (table, id, name) => db.query(`INSERT INTO ${table} (id, name) VALUES (?, ?)`).run(id, name);

const createTable = (name, attributes) => db.query(`CREATE TABLE IF NOT EXISTS ${name} (${attributes})`).run();

const getLastId = (table) => {
    const row = db.query(`SELECT MAX(id) as maxId FROM ${table}`).get();
    return row.maxId;
};

createTable("users", "id INTEGER PRIMARY KEY, name TEXT");

let i = getLastId("users") || 0;

insert("users", ++i, "Alice");