import '../models/planeta.dart';
import '../database/db_helper.dart';

class PlanetaController {
  final DBHelper _dbHelper = DBHelper();

  Future<List<Planeta>> listarPlanetas() async {
    return await _dbHelper.getPlanetas();
  }

  Future<void> adicionarPlaneta(Planeta planeta) async {
    await _dbHelper.insertPlaneta(planeta);
  }

  Future<void> atualizarPlaneta(Planeta planeta) async {
    await _dbHelper.updatePlaneta(planeta);
  }

  Future<void> deletarPlaneta(int id) async {
    await _dbHelper.deletePlaneta(id);
  }
}
  