import {Database} from "bun:sqlite";

const db = new Database("mydb.sqlite", {create: true});

export const insert = (table, id, name) => db.query(`INSERT INTO ${table} (id, name) VALUES (?, ?)`).run(id, name);

export const createTable = (name, attributes) => db.query(`CREATE TABLE IF NOT EXISTS ${name} (${attributes})`).run();

export const getLastId = (table) => {
    const row = db.query(`SELECT MAX(id) as maxId FROM ${table}`).get();
    return row.maxId;
};

export const remove = (table, id) => db.query(`DELETE FROM ${table} WHERE id = ?`).run(id);

export const select = (table, attribute, value) => db.query(`SELECT * FROM ${table} WHERE ${attribute} = ?`).all(value);

export const update = (table, id, attribute, value) => db.query(`UPDATE ${table} SET ${attribute} = ? WHERE id = ?`).run(value, id);