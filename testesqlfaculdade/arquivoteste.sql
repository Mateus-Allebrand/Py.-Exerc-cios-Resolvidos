






-- Criação do Banco de Dados
CREATE DATABASE hospedar_db;
USE hospedar_db;

-- Criação das Tabelas
CREATE TABLE Hotel (
    hotel_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    classificacao INT NOT NULL
);

CREATE TABLE Quarto (
    quarto_id INT PRIMARY KEY,
    hotel_id INT NOT NULL,
    numero INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    preco_diaria DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
);

CREATE TABLE Cliente (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE
);

CREATE TABLE Hospedagem (
    hospedagem_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    quarto_id INT NOT NULL,
    dt_checkin DATE NOT NULL,
    dt_checkout DATE NOT NULL,
    valor_total_hosp FLOAT NOT NULL,
    status_hosp VARCHAR(20) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY (quarto_id) REFERENCES Quarto(quarto_id)
);











-- Inserção de Dados Artificiais
INSERT INTO Hotel (hotel_id, nome, cidade, uf, classificacao)
VALUES (1, 'Hotel Astros', 'São Paulo', 'SP', 4),
       (2, 'Hotel Borussia', 'Rio de Janeiro', 'RJ', 5);

-- Inserir dados na tabela Quarto
INSERT INTO Quarto (quarto_id, hotel_id, numero, tipo, preco_diaria)
VALUES (1, 1, 101, 'Standard', 200.00),
       (2, 1, 102, 'Deluxe', 300.00),
       (3, 1, 103, 'Suíte', 400.00),
       (4, 1, 104, 'Standard', 200.00),
       (5, 1, 105, 'Deluxe', 300.00),
       (6, 2, 201, 'Standard', 250.00),
       (7, 2, 202, 'Deluxe', 350.00),
       (8, 2, 203, 'Suíte', 450.00),
       (9, 2, 204, 'Standard', 250.00),
       (10, 2, 205, 'Deluxe', 350.00);

-- Inserir dados na tabela Cliente
INSERT INTO Cliente (cliente_id, nome, email, telefone, cpf)
VALUES (1, 'Alexandre Reis', 'alexreis@gmail.com', '823456789', '11111111111'),
       (2, 'Marina winter', 'mariwinter@gmail.com', '987654321', '22222222222'),
       (3, 'Alminda Camardelli', 'camardellialminda@gmail.com', '986789123', '33333333333');

-- Inserir dados na tabela Hospedagem
INSERT INTO Hospedagem (hospedagem_id, cliente_id, quarto_id, dt_checkin, dt_checkout, valor_total_hosp, status_hosp)
VALUES (1, 1, 1, '2023-01-01', '2023-01-05', 800.00, 'finalizada'),
       (2, 1, 2, '2023-02-01', '2023-02-03', 600.00, 'finalizada'),
       (3, 1, 3, '2023-03-01', '2023-03-05', 1600.00, 'finalizada'),
       (4, 2, 4, '2023-04-01', '2023-04-05', 800.00, 'finalizada'),
       (5, 2, 5, '2023-05-01', '2023-05-03', 600.00, 'finalizada'),
       (6, 2, 6, '2023-06-01', '2023-06-05', 1000.00, 'hospedado'),
       (7, 3, 7, '2023-07-01', '2023-07-03', 700.00, 'hospedado'),
       (8, 3, 8, '2023-08-01', '2023-08-05', 1350.00, 'hospedado'),
       (9, 1, 9, '2023-09-01', '2023-09-05', 1250.00, 'hospedado'),
       (10, 2, 10, '2023-10-01', '2023-10-03', 700.00, 'hospedado'),
       (11, 3, 1, '2023-11-01', '2023-11-05', 800.00, 'reserva'),
       (12, 1, 2, '2023-12-01', '2023-12-03', 600.00, 'reserva'),
       (13, 2, 3, '2024-01-01', '2024-01-05', 1600.00, 'reserva'),
       (14, 3, 4, '2024-02-01', '2024-02-05', 800.00, 'reserva'),
       (15, 1, 5, '2024-03-01', '2024-03-03', 600.00, 'reserva'),
       (16, 3, 6, '2024-04-01', '2024-04-05', 1000.00, 'cancelada'),
       (17, 2, 7, '2024-05-01', '2024-05-03', 700.00, 'cancelada'),
       (18, 1, 8, '2024-06-01', '2024-06-05', 1350.00, 'cancelada'),
       (19, 3, 9, '2024-07-01', '2024-07-05', 1250.00, 'cancelada'),
       (20, 2, 10, '2024-08-01', '2024-08-03', 700.00, 'cancelada');

-- Consultas SQL

-- 4 -a

SELECT 
    h.nome AS hotel_nome,
    h.cidade AS hotel_cidade,
    q.tipo AS quarto_tipo,
    q.preco_diaria AS quarto_preco_diaria
FROM 
    Hotel h
JOIN 
    Quarto q ON h.hotel_id = q.hotel_id;

--4 -b
SELECT 
    c.nome AS cliente_nome,
    c.email AS cliente_email,
    c.telefone AS cliente_telefone,
    h.nome AS hotel_nome,
    h.cidade AS hotel_cidade,
    q.tipo AS quarto_tipo,
    q.preco_diaria AS quarto_preco_diaria,
    hs.dt_checkin,
    hs.dt_checkout,
    hs.valor_total_hosp
FROM 
    Cliente c
JOIN 
    Hospedagem hs ON c.cliente_id = hs.cliente_id
JOIN 
    Quarto q ON hs.quarto_id = q.quarto_id
JOIN 
    Hotel h ON q.hotel_id = h.hotel_id
WHERE 
    hs.status_hosp = 'finalizada';


--4 -c
SELECT 
    c.nome AS cliente_nome,
    h.nome AS hotel_nome,
    h.cidade AS hotel_cidade,
    q.tipo AS quarto_tipo,
    hs.dt_checkin,
    hs.dt_checkout,
    hs.valor_total_hosp,
    hs.status_hosp
FROM 
    Cliente c
JOIN 
    Hospedagem hs ON c.cliente_id = hs.cliente_id
JOIN 
    Quarto q ON hs.quarto_id = q.quarto_id
JOIN 
    Hotel h ON q.hotel_id = h.hotel_id
WHERE 
    c.cliente_id = 1  -- No meu exemplo,usei o id 1, mas pode
                      -- ser qualquer id desejado 
ORDER BY 
    hs.dt_checkin;

-- 4 - d   

SELECT 
    c.cliente_id,
    c.nome AS cliente_nome,
    COUNT(hs.hospedagem_id) AS total_hospedagens
FROM 
    Cliente c
LEFT JOIN 
    Hospedagem hs ON c.cliente_id = hs.cliente_id
GROUP BY 
    c.cliente_id, c.nome
ORDER BY 
    total_hospedagens DESC
LIMIT 1;

-- 4 -e

SELECT 
    c.nome AS cliente_nome,
    h.nome AS hotel_nome,
    h.cidade AS hotel_cidade,
    q.tipo AS quarto_tipo,
    hs.dt_checkin,
    hs.dt_checkout,
    hs.status_hosp
FROM 
    Cliente c
JOIN 
    Hospedagem hs ON c.cliente_id = hs.cliente_id
JOIN 
    Quarto q ON hs.quarto_id = q.quarto_id
JOIN 
    Hotel h ON q.hotel_id = h.hotel_id
WHERE 
    hs.status_hosp = 'cancelada';

-- 4 -f
SELECT 
    h.nome AS hotel_nome,
    h.cidade AS hotel_cidade,
    SUM(hs.valor_total_hosp) AS receita_total
FROM 
    Hotel h
JOIN 
    Quarto q ON h.hotel_id = q.hotel_id
JOIN 
    Hospedagem hs ON q.quarto_id = hs.quarto_id
WHERE 
    hs.status_hosp = 'finalizada'
GROUP BY 
    h.nome, h.cidade
ORDER BY 
    receita_total DESC;

-- 4 -g

SELECT DISTINCT
    c.nome AS cliente_nome,
    h.nome AS hotel_nome,
    h.cidade AS hotel_cidade
FROM 
    Cliente c
JOIN 
    Hospedagem hs ON c.cliente_id = hs.cliente_id
JOIN 
    Quarto q ON hs.quarto_id = q.quarto_id
JOIN 
    Hotel h ON q.hotel_id = h.hotel_id
WHERE 
    h.nome = 'Alminda Camardelli' -- usei o nome do cliente Alminda como exemplo
    AND hs.status_hosp = 'reserva';

--4 -h

SELECT
    c.nome AS cliente_nome,
    SUM(hs.valor_total_hosp) AS total_gasto
FROM 
    Cliente c
JOIN 
    Hospedagem hs ON c.cliente_id = hs.cliente_id
WHERE 
    hs.status_hosp = 'finalizada'
GROUP BY 
    c.cliente_id, c.nome
ORDER BY 
    total_gasto DESC;


-- 4 - i

SELECT
    q.*
FROM 
    Quarto q
LEFT JOIN 
    Hospedagem hs ON q.quarto_id = hs.quarto_id AND hs.status_hosp = 'hospedado'
WHERE 
    hs.hospedagem_id IS NULL;

-- 4 -j

SELECT
    h.nome AS hotel_nome,
    q.tipo AS quarto_tipo,
    AVG(q.preco_diaria) AS media_diaria
FROM 
    Hotel h
JOIN 
    Quarto q ON h.hotel_id = q.hotel_id
GROUP BY 
    h.nome, q.tipo
ORDER BY 
    h.nome, media_diaria DESC;


-- 4 - l




-- Adicionei via código a coluna checkin_realizado do tipo BOOLEAN na tabela Hospedagem
ALTER TABLE Hospedagem
ADD COLUMN checkin_realizado BOOLEAN;


-- Atribuí verdadeiro para hospedagens com status "finalizada" e "hospedado"
UPDATE Hospedagem
SET checkin_realizado = TRUE
WHERE status_hosp IN ('finalizada', 'hospedado');

-- Atribui falso para hospedagens com status "reserva" e "cancelada"
UPDATE Hospedagem
SET checkin_realizado = FALSE
WHERE status_hosp IN ('reserva', 'cancelada');


-- 4 -m

-- Renomeia a coluna classificacao para ratting na tabela Hotel
ALTER TABLE Hotel
RENAME COLUMN classificacao TO ratting;

-- Procedimentos usando PL/MySQL
-- (Inclua todos os procedimentos fornecidos aqui)
-- 5 -a

DELIMITER //

CREATE PROCEDURE RegistrarCheckIn(
    IN p_hospedagem_id INT,
    IN p_data_checkin DATE
)
BEGIN
    -- Atualiza a data de check-in e o status da hospedagem
    UPDATE Hospedagem
    SET dt_checkin = p_data_checkin,
        status_hosp = 'hospedado'
    WHERE hospedagem_id = p_hospedagem_id;
END //

DELIMITER ;

-- 5 -b
DELIMITER //

CREATE PROCEDURE CalcularTotalHospedagem(
    IN p_hospedagem_id INT
)
BEGIN
    DECLARE v_dt_checkin DATE;
    DECLARE v_dt_checkout DATE;
    DECLARE v_preco_diaria DECIMAL(10, 2);
    DECLARE v_total FLOAT;

    -- Obter data de check-in, data de check-out e preço da diária do quarto reservado
    SELECT dt_checkin, dt_checkout, preco_diaria
    INTO v_dt_checkin, v_dt_checkout, v_preco_diaria
    FROM Hospedagem h
    JOIN Quarto q ON h.quarto_id = q.quarto_id
    WHERE h.hospedagem_id = p_hospedagem_id;

    -- Calcular a diferença de dias entre check-in e check-out
    SET v_total = DATEDIFF(v_dt_checkout, v_dt_checkin) * v_preco_diaria;

    -- Atualizar o valor total da hospedagem na tabela Hospedagem
    UPDATE Hospedagem
    SET valor_total_hosp = v_total
    WHERE hospedagem_id = p_hospedagem_id;
END //

DELIMITER ;

-- 5 - c

DELIMITER //

CREATE PROCEDURE RegistrarCheckout(
    IN p_hospedagem_id INT,
    IN p_data_checkout DATE
)
BEGIN
    -- Atualizar a data de check-out e status_hosp na tabela Hospedagem
    UPDATE Hospedagem
    SET dt_checkout = p_data_checkout,
        status_hosp = 'finalizada'
    WHERE hospedagem_id = p_hospedagem_id;
END //

DELIMITER ;


-- 6- a

DELIMITER //

CREATE FUNCTION TotalHospedagensHotel(p_hotel_id INT) RETURNS INT
BEGIN
    DECLARE total_hospedagens INT;

    SELECT COUNT(*) INTO total_hospedagens
    FROM Hospedagem h
    JOIN Quarto q ON h.quarto_id = q.quarto_id
    WHERE q.hotel_id = p_hotel_id
    AND h.status_hosp = 'finalizada';

    RETURN total_hospedagens;
END //

DELIMITER ;

-- 6 -b

DELIMITER //

CREATE FUNCTION ValorMedioDiariasHotel(p_hotel_id INT) RETURNS DECIMAL(10,2)
BEGIN
    DECLARE media_diarias DECIMAL(10,2);

    SELECT AVG(q.preco_diaria) INTO media_diarias
    FROM Quarto q
    WHERE q.hotel_id = p_hotel_id;

    RETURN media_diarias;
END //

DELIMITER ;


--6-c

DELIMITER //

CREATE FUNCTION VerificarDisponibilidadeQuarto(p_quarto_id INT, p_data DATE) RETURNS BOOLEAN
BEGIN
    DECLARE disponivel BOOLEAN;

    SELECT COUNT(*)
    INTO disponivel
    FROM Hospedagem h
    WHERE h.quarto_id = p_quarto_id
      AND p_data BETWEEN h.dt_checkin AND h.dt_checkout
      AND h.status_hosp IN ('reserva', 'hospedado');

    RETURN NOT disponivel; -- Retorna verdadeiro se não houver hospedagens reservadas no quarto para a data especificada
END //

DELIMITER ;

-- 7 a

DELIMITER //

CREATE TRIGGER AntesDeInserirHospedagem
BEFORE INSERT ON Hospedagem
FOR EACH ROW
BEGIN
    DECLARE quarto_disponivel BOOLEAN;

    -- Verifica se o quarto está disponível na data de check-in
    SELECT NOT VerificarDisponibilidadeQuarto(NEW.quarto_id, NEW.dt_checkin)
    INTO quarto_disponivel;

    -- Se o quarto não estiver disponível, cancela a inserção
    IF NOT quarto_disponivel THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Quarto não está disponível na data de check-in. Inserção cancelada.';
    END IF;
END //

DELIMITER ;

--7 b

DELIMITER //

CREATE TRIGGER AposDeletarCliente
AFTER DELETE ON Cliente
FOR EACH ROW
BEGIN
    DECLARE cliente_nome VARCHAR(100);
    
    -- Obter o nome do cliente deletado
    SELECT nome INTO cliente_nome
    FROM Cliente
    WHERE cliente_id = OLD.cliente_id;
    
    -- Inserir registro na tabela de log
    INSERT INTO LogExclusaoCliente (cliente_id, nome_cliente, data_exclusao)
    VALUES (OLD.cliente_id, cliente_nome, NOW());
END //

DELIMITER ;

-- Funções usando PL/MySQL
-- (Inclua todas as funções fornecidas aqui)

-- Triggers usando PL/MySQL
-- (Inclua todos os triggers fornecidos aqui)
