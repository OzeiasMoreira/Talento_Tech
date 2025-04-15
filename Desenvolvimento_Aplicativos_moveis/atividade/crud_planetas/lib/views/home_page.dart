import 'package:flutter/material.dart';
import '../controllers/planeta_controller.dart';
import '../models/planeta.dart';
import 'planeta_form_page.dart';
import 'planeta_detail_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final PlanetaController _controller = PlanetaController();
  late Future<List<Planeta>> _planetasFuture;

  @override
  void initState() {
    super.initState();
    _loadPlanetas();
  }

  void _loadPlanetas() {
    setState(() {
      _planetasFuture = _controller.listarPlanetas();
    });
  }

  void _confirmarExclusao(Planeta planeta) async {
    final confirmado = await showDialog<bool>(
      context: context,
      builder: (_) => AlertDialog(
        title: Text('Excluir ${planeta.nome}?'),
        content: const Text('Deseja realmente excluir este planeta?'),
        actions: [
          TextButton(
              onPressed: () => Navigator.pop(context, false),
              child: const Text('Cancelar')),
          TextButton(
              onPressed: () => Navigator.pop(context, true),
              child: const Text('Excluir')),
        ],
      ),
    );

    if (confirmado ?? false) {
      await _controller.deletarPlaneta(planeta.id!);
      _loadPlanetas();
      ScaffoldMessenger.of(context)
          .showSnackBar(const SnackBar(content: Text('Planeta excluído.')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Planetas')),
      body: FutureBuilder<List<Planeta>>(
        future: _planetasFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting)
            return const Center(child: CircularProgressIndicator());
          if (!snapshot.hasData || snapshot.data!.isEmpty)
            return const Center(child: Text('Nenhum planeta cadastrado.'));
          final planetas = snapshot.data!;
          return ListView.builder(
            itemCount: planetas.length,
            itemBuilder: (context, index) {
              final p = planetas[index];
              return ListTile(
                title: Text(p.nome),
                subtitle: Text(p.apelido ?? 'Sem apelido'),
                onTap: () async {
                  await Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (_) => PlanetaDetailPage(planeta: p)),
                  );
                  _loadPlanetas();
                },
                trailing: IconButton(
                  icon: const Icon(Icons.delete, color: Colors.red),
                  onPressed: () => _confirmarExclusao(p),
                ),
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          await Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => const PlanetaFormPage()),
          );
          _loadPlanetas();
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
