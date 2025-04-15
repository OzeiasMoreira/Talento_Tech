import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/planeta.dart';

class DBHelper {
  static final DBHelper _instance = DBHelper._internal();
  factory DBHelper() => _instance;
  DBHelper._internal();

  Database? _db;

  Future<Database> get db async {
    if (_db != null) return _db!;
    _db = await _initDb();
    return _db!;
  }

  Future<Database> _initDb() async {
    final path = join(await getDatabasesPath(), 'planetas.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: _onCreate,
    );
  }

  Future<void> _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE planetas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        apelido TEXT,
        distanciaSol REAL NOT NULL,
        tamanho REAL NOT NULL
      )
    ''');
  }

  Future<int> insertPlaneta(Planeta planeta) async {
    final dbClient = await db;
    return await dbClient.insert('planetas', planeta.toMap());
  }

  Future<List<Planeta>> getPlanetas() async {
    final dbClient = await db;
    final maps = await dbClient.query('planetas');
    return maps.map((map) => Planeta.fromMap(map)).toList();
  }

  Future<int> updatePlaneta(Planeta planeta) async {
    final dbClient = await db;
    return await dbClient.update(
      'planetas',
      planeta.toMap(),
      where: 'id = ?',
      whereArgs: [planeta.id],
    );
  }

  Future<int> deletePlaneta(int id) async {
    final dbClient = await db;
    return await dbClient.delete('planetas', where: 'id = ?', whereArgs: [id]);
  }
}
