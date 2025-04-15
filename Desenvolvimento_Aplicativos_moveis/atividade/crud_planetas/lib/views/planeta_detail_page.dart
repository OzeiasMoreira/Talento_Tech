import 'package:flutter/material.dart';
import '../models/planeta.dart';
import 'planeta_form_page.dart';

class PlanetaDetailPage extends StatelessWidget {
  final Planeta planeta;

  const PlanetaDetailPage({super.key, required this.planeta});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(planeta.nome),
        actions: [
          IconButton(
            icon: const Icon(Icons.edit),
            onPressed: () async {
              await Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => PlanetaFormPage(planeta: planeta)),
              );
              Navigator.pop(context); // Volta pra lista após edição
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Card(
          elevation: 4,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('🌍 Nome: ${planeta.nome}', style: Theme.of(context).textTheme.titleLarge),
                const SizedBox(height: 10),
                if (planeta.apelido != null && planeta.apelido!.isNotEmpty)
                  Text('🔖 Apelido: ${planeta.apelido}', style: Theme.of(context).textTheme.bodyLarge),
                const SizedBox(height: 10),
                Text('🌞 Distância do Sol: ${planeta.distanciaSol} UA'),
                const SizedBox(height: 10),
                Text('📏 Tamanho: ${planeta.tamanho} km'),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
