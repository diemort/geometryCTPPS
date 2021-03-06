/****************************************************************************
*
* This is a part of TOTEM offline software.
* Authors: 
*  Jan Kašpar (jan.kaspar@gmail.com) 
*    
* $$RCSfile: StraightTrackAlignment.h,v $: $
* $Revision: 9977 $
* $Date: 2015-01-12 16:00:26 +0200 (pon, 12 sty 2015) $
*
****************************************************************************/

#ifndef _AlignmentConstraint_h_
#define _AlignmentConstraint_h_

#include "TotemAlignment/RPTrackBased/interface/AlignmentTask.h"

#include <TVectorD.h>

#include <map>
#include <string>

/**
 *\brief An alignment constraint.
 **/
struct AlignmentConstraint
{
  /// constraint value
  double val;

  /// map: AlignmentAlgorithm::QuantityClass -> constraint coefficients
  std::map<unsigned int, TVectorD> coef;

  /// what class is the constraint for
  AlignmentTask::QuantityClass forClass;

  /// is this an extended or basic constraint
  bool extended;

  /// label of the constraint
  std::string name;
};

#endif


