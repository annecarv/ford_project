// lib/screens/home_screen.dart

import 'package:flutter/material.dart';
import '../widgets/menu_widget.dart'; // Importe o Menu da pasta widgets

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Tela Principal'),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.menu),
            onPressed: () {
              // Ao clicar no ícone de menu, navegue para o Menu
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => Menu()),
              );
            },
          ),
        ],
      ),
      body: Center(
        child: Text('Bem-vindo à tela principal!'),
      ),
    );
  }
}
