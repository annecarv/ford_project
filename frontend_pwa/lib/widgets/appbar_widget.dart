import 'package:flutter/material.dart';

class AppbarWidget extends StatelessWidget implements PreferredSizeWidget {
  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Text('Meu Cabeçalho'),
      centerTitle: true,
      backgroundColor: Colors.blueAccent,
      leading: IconButton(
        icon: Icon(Icons.menu),
        onPressed: () {
          print('Menu clicado');
        },
      ),
      actions: [
        IconButton(
          icon: Icon(Icons.notifications),
          onPressed: () {
            print('Notificações clicadas');
          },
        ),
        IconButton(
          icon: Icon(Icons.account_circle),
          onPressed: () {
            print('Perfil clicado');
          },
        ),
      ],
    );
  }

  @override
  Size get preferredSize => Size.fromHeight(kToolbarHeight);
}
