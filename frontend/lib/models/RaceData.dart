class RaceData {
  final String name;
  final String datePretty;
  final String dateComputations;
  final String timeComputations;

  const RaceData({
    required this.name,
    required this.datePretty,
    required this.dateComputations,
    required this.timeComputations,
  });

  factory RaceData.fromJson(Map<String, dynamic> json) {
    return RaceData(
      name: json['name'],
      datePretty: json['datePretty'],
      dateComputations: json['dateComputations'],
      timeComputations: json['timeComputations'],
    );
  }
}
