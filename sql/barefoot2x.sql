/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50544
Source Host           : localhost:3306
Source Database       : barefoot2x

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2017-03-23 16:32:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for componente
-- ----------------------------
DROP TABLE IF EXISTS `componente`;
CREATE TABLE `componente` (
  `CO_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PV_RUT` char(15) COLLATE utf8_spanish_ci NOT NULL,
  `TC_ID` int(11) NOT NULL,
  `CO_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `CO_PRECIO` decimal(10,0) DEFAULT NULL,
  `CO_MARCA_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`CO_ID`),
  KEY `FK_R_17` (`PV_RUT`) USING BTREE,
  KEY `FK_R_21` (`TC_ID`) USING BTREE,
  KEY `CO_MARCA_ID` (`CO_MARCA_ID`),
  CONSTRAINT `componente_ibfk_2` FOREIGN KEY (`PV_RUT`) REFERENCES `proveedor` (`PV_RUT`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `componente_ibfk_1` FOREIGN KEY (`TC_ID`) REFERENCES `tipoc` (`TC_ID`),
  CONSTRAINT `componente_ibfk_3` FOREIGN KEY (`CO_MARCA_ID`) REFERENCES `marcas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of componente
-- ----------------------------
INSERT INTO `componente` VALUES ('1', '12546988', '1', 'Componente 01', '15000', '4');
INSERT INTO `componente` VALUES ('2', '12546988', '1', 'Componente 04', '20000', '3');
INSERT INTO `componente` VALUES ('3', '12546988', '1', 'nuevo componente', '14580', '4');

-- ----------------------------
-- Table structure for comunidad
-- ----------------------------
DROP TABLE IF EXISTS `comunidad`;
CREATE TABLE `comunidad` (
  `CM_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PA_ID` int(11) NOT NULL,
  `CM_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `CM_PAIS` char(2) COLLATE utf8_spanish_ci DEFAULT NULL,
  `CM_NUMEQUIPOS` decimal(3,0) DEFAULT NULL,
  `CM_CASAS` decimal(4,0) DEFAULT NULL,
  `CM_TIENDAS` decimal(4,0) DEFAULT NULL,
  `CM_EDIFICIOS` decimal(4,0) DEFAULT NULL,
  `CM_FIRMADO` decimal(1,0) DEFAULT NULL,
  `CM_RESERVADO` decimal(1,0) DEFAULT NULL,
  `CM_PORCINST` decimal(3,0) DEFAULT NULL,
  `CN_PERINIENT` date DEFAULT NULL,
  `CN_PERFINENT` date DEFAULT NULL,
  `CN_FECENT` date DEFAULT NULL,
  `CN_CAPACITA` decimal(1,0) DEFAULT NULL,
  `CN_CANTCAP` decimal(2,0) DEFAULT NULL,
  `CN_GENCAP` decimal(1,0) DEFAULT NULL,
  PRIMARY KEY (`CM_ID`),
  KEY `FK_R_14` (`PA_ID`) USING BTREE,
  CONSTRAINT `comunidad_ibfk_1` FOREIGN KEY (`PA_ID`) REFERENCES `pais` (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of comunidad
-- ----------------------------
INSERT INTO `comunidad` VALUES ('2', '2', 'Comunidad 02 Antofagasta', '2', '200', '100', '6', '10', '0', '1', null, null, null, null, null, null, null);
INSERT INTO `comunidad` VALUES ('3', '2', 'comarca 915', '2', '2', '12', '23', '34', '1', '1', null, null, null, null, null, null, null);
INSERT INTO `comunidad` VALUES ('5', '1', 'Tanque 500', '1', '7', '7', '10', '1', '1', '1', null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------

-- ----------------------------
-- Table structure for equipo
-- ----------------------------
DROP TABLE IF EXISTS `equipo`;
CREATE TABLE `equipo` (
  `EQ_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TE_ID` int(11) NOT NULL,
  `EQ_NOMBRE` char(50) COLLATE utf8_spanish_ci NOT NULL,
  `EQ_PRECIO` decimal(10,0) DEFAULT NULL,
  `EQ_ESTADO` decimal(1,0) DEFAULT NULL,
  PRIMARY KEY (`EQ_ID`),
  KEY `FK_R_19` (`TE_ID`) USING BTREE,
  CONSTRAINT `equipo_ibfk_1` FOREIGN KEY (`TE_ID`) REFERENCES `tipoe` (`TE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of equipo
-- ----------------------------
INSERT INTO `equipo` VALUES ('1', '1', 'Equipo 01', '150000', '1');
INSERT INTO `equipo` VALUES ('3', '2', 'Equipo 30', '10000', '1');
INSERT INTO `equipo` VALUES ('4', '1', 'Equipo 07', '1000000', '1');

-- ----------------------------
-- Table structure for equipocom
-- ----------------------------
DROP TABLE IF EXISTS `equipocom`;
CREATE TABLE `equipocom` (
  `EC_ID` int(11) NOT NULL AUTO_INCREMENT,
  `EQ_ID` int(11) NOT NULL,
  `CO_ID` int(11) NOT NULL,
  `EC_REVISION` decimal(1,0) DEFAULT NULL,
  `EC_ESTADO` decimal(1,0) DEFAULT NULL,
  `EC_PROBLEMA` char(3) COLLATE utf8_spanish_ci DEFAULT NULL,
  `EC_REPUESTO` decimal(1,0) DEFAULT NULL,
  `EC_HERRAMIENTA` decimal(1,0) DEFAULT NULL,
  `EC_HERRNOTA` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`EC_ID`),
  KEY `FK_R_10` (`EQ_ID`) USING BTREE,
  KEY `FK_R_9` (`CO_ID`) USING BTREE,
  CONSTRAINT `equipocom_ibfk_1` FOREIGN KEY (`EQ_ID`) REFERENCES `equipo` (`EQ_ID`),
  CONSTRAINT `equipocom_ibfk_2` FOREIGN KEY (`CO_ID`) REFERENCES `componente` (`CO_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of equipocom
-- ----------------------------
INSERT INTO `equipocom` VALUES ('1', '1', '1', '1', '1', '0', '0', '1', 'Nota de testing');
INSERT INTO `equipocom` VALUES ('2', '1', '2', '1', '1', '1', '1', '1', 'Nota de testing');

-- ----------------------------
-- Table structure for equipo_comunidades
-- ----------------------------
DROP TABLE IF EXISTS `equipo_comunidades`;
CREATE TABLE `equipo_comunidades` (
  `EQ_CM_ID` int(11) NOT NULL AUTO_INCREMENT,
  `EQ_ID` int(11) NOT NULL,
  `CM_ID` int(11) NOT NULL,
  PRIMARY KEY (`EQ_CM_ID`),
  KEY `equipo_comunidades_ibfk_1` (`EQ_ID`),
  KEY `equipo_comunidades_ibfk_2` (`CM_ID`),
  CONSTRAINT `equipo_comunidades_ibfk_2` FOREIGN KEY (`CM_ID`) REFERENCES `comunidad` (`CM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `equipo_comunidades_ibfk_1` FOREIGN KEY (`EQ_ID`) REFERENCES `equipo` (`EQ_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of equipo_comunidades
-- ----------------------------
INSERT INTO `equipo_comunidades` VALUES ('8', '3', '2');
INSERT INTO `equipo_comunidades` VALUES ('13', '4', '2');
INSERT INTO `equipo_comunidades` VALUES ('23', '3', '5');
INSERT INTO `equipo_comunidades` VALUES ('24', '1', '5');

-- ----------------------------
-- Table structure for herramienta
-- ----------------------------
DROP TABLE IF EXISTS `herramienta`;
CREATE TABLE `herramienta` (
  `HR_ID` int(11) NOT NULL,
  `CO_ID` int(11) NOT NULL,
  `HR_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`HR_ID`),
  KEY `FK_R_13` (`CO_ID`) USING BTREE,
  CONSTRAINT `herramienta_ibfk_1` FOREIGN KEY (`CO_ID`) REFERENCES `componente` (`CO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of herramienta
-- ----------------------------
INSERT INTO `herramienta` VALUES ('1', '1', 'der');

-- ----------------------------
-- Table structure for ingenieros_solares
-- ----------------------------
DROP TABLE IF EXISTS `ingenieros_solares`;
CREATE TABLE `ingenieros_solares` (
  `ING_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ING_NOMBRE` varchar(50) DEFAULT NULL,
  `ING_PAIS_ID` int(11) DEFAULT NULL,
  `ING_USUARIO_ID` int(11) DEFAULT NULL,
  `ING_PRECIO_DIA` int(11) DEFAULT NULL,
  PRIMARY KEY (`ING_ID`),
  KEY `ING_USUARIO_ID` (`ING_USUARIO_ID`),
  KEY `ING_PAIS_ID` (`ING_PAIS_ID`),
  CONSTRAINT `ingenieros_solares_ibfk_1` FOREIGN KEY (`ING_USUARIO_ID`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `ingenieros_solares_ibfk_2` FOREIGN KEY (`ING_PAIS_ID`) REFERENCES `pais` (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of ingenieros_solares
-- ----------------------------
INSERT INTO `ingenieros_solares` VALUES ('1', 'bacilio', '1', '2', '12000');
INSERT INTO `ingenieros_solares` VALUES ('2', 'luchin', '2', '4', '50000');
INSERT INTO `ingenieros_solares` VALUES ('3', 'Ruben', '2', '5', '12500');

-- ----------------------------
-- Table structure for marcas
-- ----------------------------
DROP TABLE IF EXISTS `marcas`;
CREATE TABLE `marcas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of marcas
-- ----------------------------
INSERT INTO `marcas` VALUES ('2', 'Caterpillar');
INSERT INTO `marcas` VALUES ('3', 'Mercedes Benz');
INSERT INTO `marcas` VALUES ('4', 'Toyota');

-- ----------------------------
-- Table structure for modulos
-- ----------------------------
DROP TABLE IF EXISTS `modulos`;
CREATE TABLE `modulos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_modulo` (`nombre`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of modulos
-- ----------------------------
INSERT INTO `modulos` VALUES ('11', 'Administracion');
INSERT INTO `modulos` VALUES ('9', 'Mantenedores');
INSERT INTO `modulos` VALUES ('7', 'Procesos');
INSERT INTO `modulos` VALUES ('8', 'Reportes');
INSERT INTO `modulos` VALUES ('13', 'Transacciones');

-- ----------------------------
-- Table structure for pais
-- ----------------------------
DROP TABLE IF EXISTS `pais`;
CREATE TABLE `pais` (
  `PA_ID` int(4) NOT NULL AUTO_INCREMENT,
  `PA_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of pais
-- ----------------------------
INSERT INTO `pais` VALUES ('1', 'Chile');
INSERT INTO `pais` VALUES ('2', 'Perú');

-- ----------------------------
-- Table structure for proveedor
-- ----------------------------
DROP TABLE IF EXISTS `proveedor`;
CREATE TABLE `proveedor` (
  `PV_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PV_RUT` char(15) COLLATE utf8_spanish_ci NOT NULL,
  `PV_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `PV_DIRECCION` char(80) COLLATE utf8_spanish_ci DEFAULT NULL,
  `PV_FONO` char(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `PV_MAIL` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `PV_FECHA` date DEFAULT NULL,
  `PV_VENTA` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`PV_ID`,`PV_RUT`),
  KEY `PV_RUT` (`PV_RUT`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of proveedor
-- ----------------------------
INSERT INTO `proveedor` VALUES ('1', '7744353-3', 'Carlos Chispas Valencia', 'Av. Alameda 03456', '97845612', 'carlos.chispas@gmail.com', '2016-12-24', '1200000');
INSERT INTO `proveedor` VALUES ('2', '12546988', 'jorge alis', 'los tamales 10000', '55268362', 'jorgegomez@gmail.com', '2015-05-20', '25');

-- ----------------------------
-- Table structure for roles
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `ing_solar` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES ('1', 'administrador6657', null, null, null);
INSERT INTO `roles` VALUES ('2', 'usuario', null, null, null);
INSERT INTO `roles` VALUES ('4', 'Mirador78', null, null, null);
INSERT INTO `roles` VALUES ('7', 'cartas', null, null, null);
INSERT INTO `roles` VALUES ('8', 'Ingeniero  Solar', null, null, '1');
INSERT INTO `roles` VALUES ('9', 'tester', null, null, null);
INSERT INTO `roles` VALUES ('10', 'tester2', null, null, null);

-- ----------------------------
-- Table structure for roles_modulos
-- ----------------------------
DROP TABLE IF EXISTS `roles_modulos`;
CREATE TABLE `roles_modulos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_rol` int(11) NOT NULL,
  `id_modulo` int(11) NOT NULL,
  `create` smallint(6) NOT NULL DEFAULT '0',
  `update` smallint(6) NOT NULL DEFAULT '0',
  `pdf` smallint(6) NOT NULL DEFAULT '0',
  `excel` smallint(6) NOT NULL DEFAULT '0',
  `delete` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id_rol` (`id_rol`) USING BTREE,
  KEY `id_modulo` (`id_modulo`) USING BTREE,
  CONSTRAINT `roles_modulos_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`),
  CONSTRAINT `roles_modulos_ibfk_2` FOREIGN KEY (`id_modulo`) REFERENCES `modulos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of roles_modulos
-- ----------------------------

-- ----------------------------
-- Table structure for tecnico
-- ----------------------------
DROP TABLE IF EXISTS `tecnico`;
CREATE TABLE `tecnico` (
  `TN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PA_ID` int(11) NOT NULL,
  `TN_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`TN_ID`),
  KEY `FK_R_20` (`PA_ID`) USING BTREE,
  CONSTRAINT `tecnico_ibfk_1` FOREIGN KEY (`PA_ID`) REFERENCES `pais` (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of tecnico
-- ----------------------------
INSERT INTO `tecnico` VALUES ('1', '1', 'Juan Perez');

-- ----------------------------
-- Table structure for tipoc
-- ----------------------------
DROP TABLE IF EXISTS `tipoc`;
CREATE TABLE `tipoc` (
  `TC_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TC_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`TC_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of tipoc
-- ----------------------------
INSERT INTO `tipoc` VALUES ('1', 'Tipo componente 01');

-- ----------------------------
-- Table structure for tipoe
-- ----------------------------
DROP TABLE IF EXISTS `tipoe`;
CREATE TABLE `tipoe` (
  `TE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TE_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`TE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of tipoe
-- ----------------------------
INSERT INTO `tipoe` VALUES ('1', 'Tipo de equipo 01');
INSERT INTO `tipoe` VALUES ('2', 'Tipo de equipo 02');

-- ----------------------------
-- Table structure for tipop
-- ----------------------------
DROP TABLE IF EXISTS `tipop`;
CREATE TABLE `tipop` (
  `TP_ID` int(11) NOT NULL AUTO_INCREMENT,
  `EC_ID` int(11) NOT NULL,
  `TP_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`TP_ID`),
  KEY `FK_R_11` (`EC_ID`) USING BTREE,
  CONSTRAINT `tipop_ibfk_1` FOREIGN KEY (`EC_ID`) REFERENCES `equipocom` (`EC_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of tipop
-- ----------------------------

-- ----------------------------
-- Table structure for trazabilidad
-- ----------------------------
DROP TABLE IF EXISTS `trazabilidad`;
CREATE TABLE `trazabilidad` (
  `TZ_ID` int(11) NOT NULL AUTO_INCREMENT,
  `EQ_ID` int(11) NOT NULL,
  `TRAZA2` char(70) COLLATE utf8_spanish_ci DEFAULT NULL,
  `TZ_FECHA` date DEFAULT NULL,
  `TRAZA4` char(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `TRAZA5` char(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `TRAZA6` char(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `TRAZA7` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`TZ_ID`),
  KEY `FK_R_16` (`EQ_ID`) USING BTREE,
  CONSTRAINT `trazabilidad_ibfk_1` FOREIGN KEY (`EQ_ID`) REFERENCES `equipo` (`EQ_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of trazabilidad
-- ----------------------------

-- ----------------------------
-- Table structure for usuarios
-- ----------------------------
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `codigo_password` varchar(255) DEFAULT NULL,
  `id_pais` int(11) DEFAULT NULL,
  `ing_precio_dia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_rol` (`id_rol`) USING BTREE,
  KEY `id_pais` (`id_pais`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`),
  CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of usuarios
-- ----------------------------
INSERT INTO `usuarios` VALUES ('2', 'victor', 'lopez', 'ciberiori', '123456', '2017-01-23 19:54:00', null, '1', 'ciberiori@gmail.com', '', '1', '8000');
INSERT INTO `usuarios` VALUES ('4', 'danilo', 'lopez', 'danix2', '123456', null, null, '8', 'danilo@gmail.com', '', '2', '14500');
INSERT INTO `usuarios` VALUES ('5', 'Ruben', 'Lorca', 'rlorca', '123456', null, null, '8', 'ciberiori@gmail.com', '', '2', '1500');
