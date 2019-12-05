CREATE SCHEMA `Interview` ;

USE `Interview`;

CREATE TABLE `Interview`.`Site` (
  `idSite` INT NOT NULL,
  `SiteName` VARCHAR(45) NOT NULL,
  `State` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSite`));
  
INSERT INTO `Interview`.`Site` (`idSite`, `SiteName`, `State`) VALUES 
('0', 'Milton', 'MA'), 
('1', 'Cougar', 'NC'), 
('2', 'Champion', 'SC'), 
('3', 'Alfred', 'ON'), 
('4', 'Boxford', 'NH');

CREATE TABLE `Interview`.`Panel` (
  `idPanel` INT NOT NULL,
  `Brand` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Power` INT NOT NULL,
  PRIMARY KEY (`idPanel`));
  
INSERT INTO `Interview`.`Panel` (`idPanel`, `Brand`, `Model`, `Power`) VALUES 
('0', 'Trina Solar', 'TSM-245PC05', '245'), 
('1', 'Canadian Solar', 'CS6P-260P', '260'),
('2', 'Hanwha', 'O.Plus L-G4.2', '345'),
('3', 'Jinko', 'JKM320PP-72-V', '320'),
('4', 'JA SOLAR', 'JAP6-72-290', '290');

CREATE TABLE `Interview`.`Issue` (
  `idIssue` INT NOT NULL AUTO_INCREMENT,
  `Site` INT NOT NULL,
  `Panel` INT NOT NULL,
  `Comment` TEXT(200) NULL,
  PRIMARY KEY (`idIssue`),
  INDEX `site_idx` (`Site` ASC),
  INDEX `panel_idx` (`Panel` ASC),
  CONSTRAINT `site`
    FOREIGN KEY (`Site`)
    REFERENCES `Interview`.`Site` (`idSite`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `panel`
    FOREIGN KEY (`Panel`)
    REFERENCES `Interview`.`Panel` (`idPanel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO `Interview`.`Issue` (`idIssue`, `Site`, `Panel`, `Comment`) VALUES 
('0', '0', '1', 'Hot spot all over the panel'),
('1', '0', '1', 'Panel cracked'),
('2', '0', '3', 'Lightning strike'),
('3', '2', '2', 'Diode bypass');
