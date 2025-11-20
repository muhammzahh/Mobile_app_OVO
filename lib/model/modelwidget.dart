import 'package:flutter/material.dart';

class Modelwidget extends StatelessWidget {
  showfullmodelwidget(context, Widget isi) {
    showGeneralDialog (
      context: context, 
      barrierDismissible: false,
      barrierLabel: 'Label',);
  }



  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}