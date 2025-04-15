import 'package:flutter/material.dart';
import '../models/planeta.dart';
import '../controllers/planeta_controller.dart';

class PlanetaFormPage extends StatefulWidget {
  final Planeta? planeta;

  const PlanetaFormPage({super.key, this.planeta});

  @override
  State<PlanetaFormPage> createState() => _PlanetaFormPageState();
}

class _PlanetaFormPageState extends State<PlanetaFormPage> {
  final _formKey = GlobalKey<FormState>();
  final _controller = PlanetaController();

  late TextEditingController _nomeController;
  late TextEditingController _apelidoController;
  late TextEditingController _distanciaController;
  late TextEditingController _tamanhoController;

  @override
  void initState() {
    super.initState();
    _nomeController = TextEditingController(text: widget.planeta?.nome ?? '');
    _apelidoController = TextEditingController(text: widget.planeta?.apelido ?? '');
    _distanciaController = TextEditingController(text: widget.planeta?.distanciaSol.toString() ?? '');
    _tamanhoController = TextEditingController(text: widget.planeta?.tamanho.toString() ?? '');
  }

  @override
  void dispose() {
    _nomeController.dispose();
    _apelidoController.dispose();
    _distanciaController.dispose();
    _tamanhoController.dispose();
    super.dispose();
  }

  void _salvar() async {
    if (_formKey.currentState!.validate()) {
      final planeta = Planeta(
        id: widget.planeta?.id,
        nome: _nomeController.text,
        apelido: _apelidoController.text.isEmpty ? null : _apelidoController.text,
        distanciaSol: double.parse(_distanciaController.text),
        tamanho: double.parse(_tamanhoController.text),
      );

      if (widget.planeta == null) {
        await _controller.adicionarPlaneta(planeta);
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Planeta adicionado com sucesso!')));
      } else {
        await _controller.atualizarPlaneta(planeta);
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Planeta atualizado com sucesso!')));
      }

      Navigator.pop(context);
    }
  }

  String? _validaCampo(String? valor, {bool numerico = false}) {
    if (valor == null || valor.isEmpty) return 'Campo obrigatório';
    if (numerico && (double.tryParse(valor) == null || double.parse(valor) <= 0)) {
      return 'Informe um número válido e positivo';
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    final editando = widget.planeta != null;

    return Scaffold(
      appBar: AppBar(title: Text(editando ? 'Editar Planeta' : 'Novo Planeta')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              TextFormField(
                controller: _nomeController,
                decoration: const InputDecoration(labelText: 'Nome do Planeta'),
                validator: _validaCampo,
              ),
              TextFormField(
                controller: _apelidoController,
                decoration: const InputDecoration(labelText: 'Apelido (opcional)'),
              ),
              TextFormField(
                controller: _distanciaController,
                decoration: const InputDecoration(labelText: 'Distância do Sol (UA)'),
                keyboardType: TextInputType.number,
                validator: (v) => _validaCampo(v, numerico: true),
              ),
              TextFormField(
                controller: _tamanhoController,
                decoration: const InputDecoration(labelText: 'Tamanho (km)'),
                keyboardType: TextInputType.number,
                validator: (v) => _validaCampo(v, numerico: true),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: _salvar,
                child: Text(editando ? 'Atualizar' : 'Salvar'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
