import { Database } from "bun:sqlite";

let db;

let autoIncrement;

export const setupDB = (dbName, autoIncrementId = false) => {
  db = new Database(dbName, { create: true });
  autoIncrement = autoIncrementId;
};

export const insert = (table, attributes, autoIncrementId = false) => {
  autoIncrementId = Boolean(autoIncrementId); // Ensure autoIncrementId is a boolean

  if (autoIncrementId || autoIncrement) {
    const lastId = getLastId(table);
    attributes.id = lastId ? lastId + 1 : 1; // If lastId exists, increment it. Otherwise, start at 1.
  }

  const keys = Object.keys(attributes).join(", ");
  const values = Object.values(attributes);
  const placeholders = values.map(() => "?").join(", ");

  db.query(`INSERT INTO ${table} (${keys}) VALUES (${placeholders})`).run(
    ...values
  );
};

export const createTable = (name, attributes) =>
  db.query(`CREATE TABLE IF NOT EXISTS ${name} (${attributes})`).run();

export const getLastId = (table) => {
  const row = db.query(`SELECT MAX(id) as maxId FROM ${table}`).get();
  return row.maxId;
};

export const remove = (table, attribute, value) =>
  db.query(`DELETE FROM ${table} WHERE ${attribute} = ?`).run(value);

export const select = (table, attribute, value) => {
  const result = db
    .query(`SELECT * FROM ${table} WHERE ${attribute} = ?`)
    .all(value);
  return result.length === 1 ? result[0] : result;
};

export const update = (table, searchAttribute, searchValue, attribute, value) =>
  db
    .query(`UPDATE ${table} SET ${attribute} = ? WHERE ${searchAttribute} = ?`)
    .run(value, searchValue);
