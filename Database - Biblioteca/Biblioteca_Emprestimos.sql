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
-- Table structure for table `Emprestimos`
--

DROP TABLE IF EXISTS `Emprestimos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Emprestimos` (
  `IDEmprestimo` int NOT NULL AUTO_INCREMENT,
  `IDUsuario` int NOT NULL,
  `IDLivro` int NOT NULL,
  `dataSaida` datetime NOT NULL,
  `dataDevolucao` datetime NOT NULL,
  PRIMARY KEY (`IDEmprestimo`),
  KEY `IDUsuario` (`IDUsuario`),
  KEY `IDLivro` (`IDLivro`),
  CONSTRAINT `Emprestimos_ibfk_1` FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios` (`IDUsuario`),
  CONSTRAINT `Emprestimos_ibfk_2` FOREIGN KEY (`IDLivro`) REFERENCES `Livros` (`IDLivro`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Emprestimos`
--

LOCK TABLES `Emprestimos` WRITE;
/*!40000 ALTER TABLE `Emprestimos` DISABLE KEYS */;
INSERT INTO `Emprestimos` VALUES (1,2,1,'2010-12-10 00:00:00','2010-12-30 00:00:00'),(2,3,1,'2010-12-10 00:00:00','2010-12-25 00:00:00');
/*!40000 ALTER TABLE `Emprestimos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-31 10:57:14
