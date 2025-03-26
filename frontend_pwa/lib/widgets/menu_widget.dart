// lib/widgets/menu.dart

import 'package:flutter/material.dart';
import '../services/api_service.dart';

class MenuWidget extends StatelessWidget {
  final ApiService apiService = ApiService();

  // Função para processar a escolha do usuário
  void _handleMenuOption(String option) async {
    try {
      if (option == 'Veículos') {
        var vehicles = await apiService.getVehicles();
        print('Dados dos veículos: $vehicles');
      } else if (option == 'Garantias') {
        var warranties = await apiService.getWarranties();
        print('Dados das garantias: $warranties');
      } else if (option == 'Localizações') {
        var locations = await apiService.getLocations();
        print('Dados das localizações: $locations');
      } else {
        print('Opção não identificada');
      }
    } catch (error) {
      print('Erro ao carregar dados: $error');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Menu')),
      body: ListView(
        children: [
          ListTile(
            title: Text('Veículos'),
            onTap: () => _handleMenuOption('Veículos'),
          ),
          ListTile(
            title: Text('Garantias'),
            onTap: () => _handleMenuOption('Garantias'),
          ),
          ListTile(
            title: Text('Localizações'),
            onTap: () => _handleMenuOption('Localizações'),
          ),
        ],
      ),
    );
  }
}
