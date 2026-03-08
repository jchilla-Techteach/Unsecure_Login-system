DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('teacher', 'password123');
INSERT INTO users (username, password) VALUES ('student', 'abc123');
INSERT INTO users (username, password) VALUES ('admin', 'admin');