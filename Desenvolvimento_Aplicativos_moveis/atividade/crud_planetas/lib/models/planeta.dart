class Planeta {
  int? id;
  String nome;
  String? apelido;
  double distanciaSol; 
  double tamanho; 

  Planeta({
    this.id,
    required this.nome,
    this.apelido,
    required this.distanciaSol,
    required this.tamanho,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'nome': nome,
      'apelido': apelido,
      'distanciaSol': distanciaSol,
      'tamanho': tamanho,
    };
  }

  factory Planeta.fromMap(Map<String, dynamic> map) {
    return Planeta(
      id: map['id'],
      nome: map['nome'],
      apelido: map['apelido'],
      distanciaSol: map['distanciaSol'],
      tamanho: map['tamanho'],
    );
  }
}
