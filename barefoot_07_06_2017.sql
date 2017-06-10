/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50544
Source Host           : localhost:3306
Source Database       : barefoot2x

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2017-06-07 23:50:25
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
  KEY `componente_ibfk_1` (`CO_MARCA_ID`),
  CONSTRAINT `componente_ibfk_1` FOREIGN KEY (`CO_MARCA_ID`) REFERENCES `marcas` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `componente_ibfk_2` FOREIGN KEY (`PV_RUT`) REFERENCES `proveedor` (`PV_RUT`),
  CONSTRAINT `componente_ibfk_3` FOREIGN KEY (`TC_ID`) REFERENCES `tipoc` (`TC_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of componente
-- ----------------------------
INSERT INTO `componente` VALUES ('6', '12546988', '1', 'ruedas de camion algibe', '12500', '5');
INSERT INTO `componente` VALUES ('7', '7744353-3', '1', 'otro componente', '2500000', '6');

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
  `CM_DOC_DONACION_COMITE` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `CM_DOC_CMI` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `CM_DOC_CUENTA_BANCARIA` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`CM_ID`),
  KEY `FK_R_14` (`PA_ID`) USING BTREE,
  CONSTRAINT `comunidad_ibfk_1` FOREIGN KEY (`PA_ID`) REFERENCES `pais` (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of comunidad
-- ----------------------------
INSERT INTO `comunidad` VALUES ('2', '2', 'Comunidad 02 Antofagasta', '2', '200', '100', '6', '10', '0', '1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `comunidad` VALUES ('3', '2', 'comarca 915', '2', '2', '12', '23', '34', '1', '1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `comunidad` VALUES ('5', '1', 'comunidad especial', '1', '3', '3', '3', '5', '1', '1', null, null, null, null, null, null, null, 'daef158167004b001b458e8ae82f3c11.pdf', 'cdcc291607ff3f60c1ac34c49968c12c.pdf', '55b0677287985e8eee46fc2df6b8c509.pdf');
INSERT INTO `comunidad` VALUES ('7', '5', 'comunidad chile', '5', '2', '2', '2', '2', '1', '0', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `comunidad` VALUES ('8', '1', 'comunidad chile', '1', '3', '3', '4', '5', '1', '0', null, null, null, null, null, null, null, 'cc102d769f920269ef274f2d298c7b94.pdf', '9a36061a48da618b51354b8dc2ccf5d0.pdf', null);
INSERT INTO `comunidad` VALUES ('11', '1', 'comunidad la granja de', '1', '43', '44', '54', '12', '1', '0', null, null, null, null, null, null, null, 'd7ab93fdfec83c2755c473e0d2e83192.pdf', '9d86f3ecfc310fd38f63399c351c6ee3.pdf', '1f929676367aeda7f379e24ea466f3e8.pdf');
INSERT INTO `comunidad` VALUES ('12', '11', 'Comunidad Nuevo ghinea', '11', '15', '18', '25', '1', '1', '1', null, null, null, null, null, null, null, 'abf9bc7f3528d0f02561477c9806572e.docx', null, null);
INSERT INTO `comunidad` VALUES ('13', '1', 'comunidad responix', '1', '5', '10', '12', '0', '1', '0', null, null, null, null, null, null, null, '1d287424f7b7e068928a1b725e53fe3d.docx', null, null);

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
  `EQ_DOC_CONTRATO` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`EQ_ID`),
  KEY `FK_R_19` (`TE_ID`) USING BTREE,
  CONSTRAINT `equipo_ibfk_1` FOREIGN KEY (`TE_ID`) REFERENCES `tipoe` (`TE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of equipo
-- ----------------------------
INSERT INTO `equipo` VALUES ('3', '2', 'Equipo 30', '0', '1', 'fd7458b38bc16ee5ab868403bbce9181.docx');
INSERT INTO `equipo` VALUES ('4', '1', 'Equipo 07', '1000000', '1', 'c604c48041b6a39c277d53a60418134e.docx');
INSERT INTO `equipo` VALUES ('6', '1', 'equipo 6', '0', '0', null);
INSERT INTO `equipo` VALUES ('7', '2', 'Equipo 3', '0', '1', null);
INSERT INTO `equipo` VALUES ('8', '1', 'equipo x1', '0', '1', null);
INSERT INTO `equipo` VALUES ('9', '1', 'equipo x2', '0', '0', null);
INSERT INTO `equipo` VALUES ('10', '2', 'equipo x3', '0', '0', null);
INSERT INTO `equipo` VALUES ('11', '1', 'equipo x5', '0', '0', null);
INSERT INTO `equipo` VALUES ('12', '1', 'equipo nuevo', '0', '1', null);
INSERT INTO `equipo` VALUES ('13', '1', 'equipo nuevo 2', '0', '1', null);

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
  `EC_REPUESTO_ASIGNADO` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`EC_ID`),
  KEY `FK_R_10` (`EQ_ID`) USING BTREE,
  KEY `FK_R_9` (`CO_ID`) USING BTREE,
  CONSTRAINT `equipocom_ibfk_1` FOREIGN KEY (`EQ_ID`) REFERENCES `equipo` (`EQ_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `equipocom_ibfk_2` FOREIGN KEY (`CO_ID`) REFERENCES `componente` (`CO_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of equipocom
-- ----------------------------
INSERT INTO `equipocom` VALUES ('14', '3', '6', null, null, '', null, null, '', '1');
INSERT INTO `equipocom` VALUES ('15', '8', '7', null, null, null, null, null, null, '1');
INSERT INTO `equipocom` VALUES ('17', '11', '6', null, null, '', null, null, '', '0');
INSERT INTO `equipocom` VALUES ('18', '12', '6', null, null, '', null, null, '', '0');

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
  CONSTRAINT `equipo_comunidades_ibfk_1` FOREIGN KEY (`EQ_ID`) REFERENCES `equipo` (`EQ_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `equipo_comunidades_ibfk_2` FOREIGN KEY (`CM_ID`) REFERENCES `comunidad` (`CM_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of equipo_comunidades
-- ----------------------------
INSERT INTO `equipo_comunidades` VALUES ('8', '3', '2');
INSERT INTO `equipo_comunidades` VALUES ('13', '4', '2');
INSERT INTO `equipo_comunidades` VALUES ('23', '3', '5');
INSERT INTO `equipo_comunidades` VALUES ('28', '4', '12');
INSERT INTO `equipo_comunidades` VALUES ('29', '6', '12');
INSERT INTO `equipo_comunidades` VALUES ('30', '7', '8');
INSERT INTO `equipo_comunidades` VALUES ('31', '4', '8');
INSERT INTO `equipo_comunidades` VALUES ('32', '6', '8');
INSERT INTO `equipo_comunidades` VALUES ('33', '3', '8');
INSERT INTO `equipo_comunidades` VALUES ('34', '8', '5');
INSERT INTO `equipo_comunidades` VALUES ('35', '9', '5');
INSERT INTO `equipo_comunidades` VALUES ('36', '10', '5');
INSERT INTO `equipo_comunidades` VALUES ('37', '11', '5');
INSERT INTO `equipo_comunidades` VALUES ('38', '8', '11');
INSERT INTO `equipo_comunidades` VALUES ('39', '8', '13');
INSERT INTO `equipo_comunidades` VALUES ('40', '3', '13');
INSERT INTO `equipo_comunidades` VALUES ('41', '12', '5');

-- ----------------------------
-- Table structure for herramienta
-- ----------------------------
DROP TABLE IF EXISTS `herramienta`;
CREATE TABLE `herramienta` (
  `HR_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CO_ID` int(11) NOT NULL,
  `HR_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`HR_ID`),
  KEY `FK_R_13` (`CO_ID`) USING BTREE,
  CONSTRAINT `herramienta_ibfk_1` FOREIGN KEY (`CO_ID`) REFERENCES `componente` (`CO_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of herramienta
-- ----------------------------
INSERT INTO `herramienta` VALUES ('1', '6', 'herramenta1');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of marcas
-- ----------------------------
INSERT INTO `marcas` VALUES ('5', 'mitsubishi');
INSERT INTO `marcas` VALUES ('6', 'fujitsu2');

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
INSERT INTO `modulos` VALUES ('7', 'Consultas');
INSERT INTO `modulos` VALUES ('8', 'Control');
INSERT INTO `modulos` VALUES ('9', 'Mantenedores');

-- ----------------------------
-- Table structure for pais
-- ----------------------------
DROP TABLE IF EXISTS `pais`;
CREATE TABLE `pais` (
  `PA_ID` int(4) NOT NULL AUTO_INCREMENT,
  `PA_NOMBRE` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of pais
-- ----------------------------
INSERT INTO `pais` VALUES ('1', 'Chile');
INSERT INTO `pais` VALUES ('2', 'Perú');
INSERT INTO `pais` VALUES ('4', 'Honduras');
INSERT INTO `pais` VALUES ('5', 'Colombia');
INSERT INTO `pais` VALUES ('9', 'indonesia');
INSERT INTO `pais` VALUES ('10', 'canada');
INSERT INTO `pais` VALUES ('11', 'pakistan');
INSERT INTO `pais` VALUES ('12', 'brazil');
INSERT INTO `pais` VALUES ('13', 'argentina');
INSERT INTO `pais` VALUES ('14', 'venezuela');
INSERT INTO `pais` VALUES ('15', 'Ecuador');
INSERT INTO `pais` VALUES ('16', 'ghana2');

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
  KEY `PV_RUT` (`PV_RUT`),
  KEY `PV_ID` (`PV_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES ('1', 'administrador', null, null, null);
INSERT INTO `roles` VALUES ('2', 'usuario', null, null, null);
INSERT INTO `roles` VALUES ('4', 'Mirador78', null, null, null);
INSERT INTO `roles` VALUES ('7', 'cartas', null, null, null);
INSERT INTO `roles` VALUES ('8', 'Ingeniero  Solar', null, null, '1');
INSERT INTO `roles` VALUES ('9', 'tester', null, null, null);
INSERT INTO `roles` VALUES ('10', 'tester2', null, null, null);
INSERT INTO `roles` VALUES ('11', 'campesino', null, null, null);
INSERT INTO `roles` VALUES ('12', 'jiujitsero', null, null, null);

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
  `assign` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_rol` (`id_rol`) USING BTREE,
  KEY `id_modulo` (`id_modulo`) USING BTREE,
  CONSTRAINT `roles_modulos_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`),
  CONSTRAINT `roles_modulos_ibfk_2` FOREIGN KEY (`id_modulo`) REFERENCES `submodulos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of roles_modulos
-- ----------------------------
INSERT INTO `roles_modulos` VALUES ('5', '2', '9', '1', '1', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('106', '1', '11', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('107', '1', '10', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('108', '1', '12', '1', '1', '1', '1', '1', '1');
INSERT INTO `roles_modulos` VALUES ('109', '1', '1', '1', '1', '0', '0', '1', '0');
INSERT INTO `roles_modulos` VALUES ('110', '1', '3', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('111', '1', '2', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('112', '1', '5', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('113', '1', '4', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('114', '1', '7', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('115', '1', '6', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('116', '1', '9', '1', '0', '0', '0', '0', '0');
INSERT INTO `roles_modulos` VALUES ('117', '1', '8', '1', '0', '0', '0', '0', '0');

-- ----------------------------
-- Table structure for submodulos
-- ----------------------------
DROP TABLE IF EXISTS `submodulos`;
CREATE TABLE `submodulos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `modulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `modulo_id` (`modulo_id`),
  CONSTRAINT `submodulos_ibfk_1` FOREIGN KEY (`modulo_id`) REFERENCES `modulos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of submodulos
-- ----------------------------
INSERT INTO `submodulos` VALUES ('1', 'Paises', '9');
INSERT INTO `submodulos` VALUES ('2', 'Comunidades', '9');
INSERT INTO `submodulos` VALUES ('3', 'Equipos', '9');
INSERT INTO `submodulos` VALUES ('4', 'Componentes', '9');
INSERT INTO `submodulos` VALUES ('5', 'Talleres Solares', '9');
INSERT INTO `submodulos` VALUES ('6', 'Herramientas', '9');
INSERT INTO `submodulos` VALUES ('7', 'Marcas', '9');
INSERT INTO `submodulos` VALUES ('8', 'Proveedores', '9');
INSERT INTO `submodulos` VALUES ('9', 'Equipos Comunidad', '7');
INSERT INTO `submodulos` VALUES ('10', 'Ingenieros Por Pais', '7');
INSERT INTO `submodulos` VALUES ('11', 'Usuarios', '8');
INSERT INTO `submodulos` VALUES ('12', 'Roles', '8');

-- ----------------------------
-- Table structure for talleres_solares
-- ----------------------------
DROP TABLE IF EXISTS `talleres_solares`;
CREATE TABLE `talleres_solares` (
  `TS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TS_LUGAR` varchar(50) DEFAULT NULL,
  `TS_DIAS_USO_INGENIEROS` int(30) DEFAULT NULL,
  `TS_DIAS_USO_COMUNIDAD` int(30) DEFAULT NULL,
  `TS_CM_ID` int(11) DEFAULT NULL,
  `TS_DESCRIPCION` char(100) DEFAULT NULL,
  `TS_HABILITADO` decimal(1,0) DEFAULT NULL,
  PRIMARY KEY (`TS_ID`),
  KEY `TS_CM_ID` (`TS_CM_ID`),
  CONSTRAINT `talleres_solares_ibfk_1` FOREIGN KEY (`TS_CM_ID`) REFERENCES `comunidad` (`CM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of talleres_solares
-- ----------------------------
INSERT INTO `talleres_solares` VALUES ('1', 'españa 1234', '12', '12', '5', 'descripcion de comunidad especial', '1');
INSERT INTO `talleres_solares` VALUES ('4', 'taller solar 8', '10', '15', '8', 'taller solar dentro de la comunidad', '0');
INSERT INTO `talleres_solares` VALUES ('5', 'taller solar pakistan', '7', '7', '12', 'descripcion de comunidad dentro de la nueva guinea', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- ----------------------------
-- Records of tipoe
-- ----------------------------
INSERT INTO `tipoe` VALUES ('1', 'Tipo de equipo 01');
INSERT INTO `tipoe` VALUES ('2', 'Tipo de equipo 02');
INSERT INTO `tipoe` VALUES ('3', 'Tipo de equipo 03');

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

-- ----------------------------
-- Table structure for usuarios_paises
-- ----------------------------
DROP TABLE IF EXISTS `usuarios_paises`;
CREATE TABLE `usuarios_paises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `pais_id` (`pais_id`),
  CONSTRAINT `usuarios_paises_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `usuarios_paises_ibfk_2` FOREIGN KEY (`pais_id`) REFERENCES `pais` (`PA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of usuarios_paises
-- ----------------------------
INSERT INTO `usuarios_paises` VALUES ('3', '2', '9');
INSERT INTO `usuarios_paises` VALUES ('4', '2', '2');
INSERT INTO `usuarios_paises` VALUES ('6', '2', '14');
INSERT INTO `usuarios_paises` VALUES ('7', '2', '4');
INSERT INTO `usuarios_paises` VALUES ('8', '2', '5');
INSERT INTO `usuarios_paises` VALUES ('9', '2', '15');
INSERT INTO `usuarios_paises` VALUES ('10', '4', '13');
INSERT INTO `usuarios_paises` VALUES ('11', '4', '11');
INSERT INTO `usuarios_paises` VALUES ('12', '2', '11');
