-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: Biblioteca
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.22.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Livros`
--

DROP TABLE IF EXISTS `Livros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Livros` (
  `IDLivro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(40) NOT NULL,
  `genero` varchar(15) DEFAULT NULL,
  `ano` int DEFAULT NULL,
  `situacao` varchar(10) NOT NULL DEFAULT 'Disponível',
  `precoCusto` decimal(6,2) NOT NULL,
  PRIMARY KEY (`IDLivro`),
  CONSTRAINT `Livros_chk_1` CHECK ((`situacao` in (_utf8mb4'Emprestado',_utf8mb4'Disponível')))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Livros`
--

LOCK TABLES `Livros` WRITE;
/*!40000 ALTER TABLE `Livros` DISABLE KEYS */;
INSERT INTO `Livros` VALUES (1,'SQL Guide','Informática',2010,'Disponível',200.00),(2,'Banco de Dados',NULL,2008,'Emprestado',100.00),(3,'Manual SQL','Informática',2014,'Disponível',150.00),(4,'Manual Java','Informática',2020,'Disponível',300.00),(5,'Inteligência Artificial','Informática',2021,'Disponível',500.00);
/*!40000 ALTER TABLE `Livros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-31 10:57:13
