import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Layout Responsivo',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: ResponsiveLayout(),
    );
  }
}

class ResponsiveLayout extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Layout Responsivo'),
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          if (constraints.maxWidth < 600) {
            return Column(
              children: [
                _buildContainer(Colors.red, 'Layout Pequeno'),
                _buildContainer(Colors.blue, 'Mais Informações'),
              ],
            );
          } else {
            return Row(
              children: [
                Expanded(child: _buildContainer(Colors.red, 'Layout Grande')),
                Expanded(child: _buildContainer(Colors.blue, 'Mais Informações')),
              ],
            );
          }
        },
      ),
    );
  }

  Widget _buildContainer(Color color, String text) {
    return Container(
      color: color,
      height: 200,
      child: Center(
        child: Text(
          text,
          style: TextStyle(color: Colors.white, fontSize: 18),
        ),
      ),
    );
  }
}
