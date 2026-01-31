class RaceData {
  final String name;
  final String datePretty;
  final String dateComputations;

  const RaceData({
    required this.name,
    required this.datePretty,
    required this.dateComputations,
  });

  factory RaceData.fromJson(Map<String, dynamic> json) {
    return RaceData(
      name: json['name'],
      datePretty: json['datePretty'],
      dateComputations: json['dateComputations'],
    );
  }
}
