CREATE TABLE IF NOT EXISTS specie(
    specie_id INT,
    name TEXT,
    PRIMARY KEY(specie_id)
);

CREATE TABLE IF NOT EXISTS ant(
    ant_id TEXT,
    specie_id INT,
    PRIMARY KEY(ant_id),
    FOREIGN KEY(specie_id) REFERENCES specie(specie_id)
);

CREATE TABLE IF NOT EXISTS chamber(
    chamber_id INT,
    PRIMARY KEY(chamber_id)
);

CREATE TABLE IF NOT EXISTS tracking(
    time INT,
    x INT,
    y INT,
    ant_id TEXT,
    chamber_id INT,
    PRIMARY KEY(time, ant_id),
    FOREIGN KEY(chamber_id) REFERENCES chamber(chamber_id),
    FOREIGN KEY(ant_id) REFERENCES ant(ant_id)
);

CREATE TABLE IF NOT EXISTS trophallaxis(
    chamber_id INT,
    ant1_id TEXT,
    ant2_id TEXT,
    start_time INT,
    end_time INT,
    PRIMARY KEY(ant1_id, ant2_id, start_time),
    FOREIGN KEY(chamber_id) REFERENCES chamber(chamber_id),
    FOREIGN KEY(ant1_id) REFERENCES ant(ant_id),
    FOREIGN KEY(ant2_id) REFERENCES ant(ant_id)
);