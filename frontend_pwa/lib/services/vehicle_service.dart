import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/foundation.dart';
import '../utils/constants.dart';  // Contém os endpoints

class VehicleService {
  // Obter todos os veículos
  Future<void> getVehicles() async {
    try {
      final response = await http.get(Uri.parse(ApiConstants.vehiclesEndpoint));

      if (response.statusCode == 200) {
        debugPrint('Dados dos veículos: ${response.body}');
      } else {
        throw Exception('Falha ao carregar veículos');
      }
    } catch (error) {
      debugPrint('Erro ao buscar veículos: $error');
    }
  }

  // Obter um veículo por ID
  Future<void> getVehicleById(int vehicleId) async {
    try {
      final response = await http.get(Uri.parse('${ApiConstants.vehiclesEndpoint}/$vehicleId'));

      if (response.statusCode == 200) {
        debugPrint('Dados do veículo: ${response.body}');
      } else {
        throw Exception('Falha ao carregar o veículo');
      }
    } catch (error) {
      debugPrint('Erro ao buscar veículo: $error');
    }
  }

  // Criar um novo veículo
  Future<void> createVehicle(Map<String, dynamic> vehicleData) async {
    try {
      final response = await http.post(
        Uri.parse(ApiConstants.vehiclesEndpoint),
        headers: <String, String>{'Content-Type': 'application/json'},
        body: jsonEncode(vehicleData),
      );

      if (response.statusCode == 201) {
        debugPrint('Veículo criado: ${response.body}');
      } else {
        throw Exception('Falha ao criar veículo');
      }
    } catch (error) {
      debugPrint('Erro ao criar veículo: $error');
    }
  }

  // Atualizar um veículo existente
  Future<void> updateVehicle(int vehicleId, Map<String, dynamic> vehicleData) async {
    try {
      final response = await http.put(
        Uri.parse('${ApiConstants.vehiclesEndpoint}/$vehicleId'),
        headers: <String, String>{'Content-Type': 'application/json'},
        body: jsonEncode(vehicleData),
      );

      if (response.statusCode == 200) {
        debugPrint('Veículo atualizado: ${response.body}');
      } else {
        throw Exception('Falha ao atualizar veículo');
      }
    } catch (error) {
      debugPrint('Erro ao atualizar veículo: $error');
    }
  }

  // Deletar um veículo
  Future<void> deleteVehicle(int vehicleId) async {
    try {
      final response = await http.delete(Uri.parse('${ApiConstants.vehiclesEndpoint}/$vehicleId'));

      if (response.statusCode == 200) {
        debugPrint('Veículo deletado: ${response.body}');
      } else {
        throw Exception('Falha ao deletar veículo');
      }
    } catch (error) {
      debugPrint('Erro ao deletar veículo: $error');
    }
  }
}
