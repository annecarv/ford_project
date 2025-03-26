import 'package:flutter/material.dart';
import '../services/vehicle_service.dart';

class VehicleScreen extends StatelessWidget {
  final VehicleService _vehicleService = VehicleService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Veículos'),
      ),
      body: FutureBuilder(
        future: _vehicleService.getVehicles(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Erro: ${snapshot.error}'));
          }
          return Center(child: Text('Dados dos veículos carregados.'));
        },
      ),
    );
  }
}
