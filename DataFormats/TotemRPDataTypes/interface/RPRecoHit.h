/****************************************************************************
*
* This is a part of TOTEM offline software.
* Authors:
*   Hubert Niewiadomski
*   Jan Kašpar (jan.kaspar@gmail.com)
*
****************************************************************************/

#ifndef DataFormats_TotemRPDataTypes_RPRecoHit_h_
#define DataFormats_TotemRPDataTypes_RPRecoHit_h_

#include "DataFormats/TotemRPDataTypes/interface/RPTypes.h"

/**
 *\brief Reconstructed hit in RP.
 *
 * Representation of a strip cluster (RPDigCluster), the position of which has been converted into mm
 * (see RPTopology::GetHitPositionInReadoutDirection).
 **/
class RPRecoHit
{
 public:
  RPRecoHit(RPDetId det_id, double position, double sigma) : det_id_(det_id), 
    position_(position), sigma_(sigma) {}
  RPRecoHit() : det_id_(0), position_(0), sigma_(0) {}

  inline double Position() const {return position_;}
  inline void Position(double position) {position_=position;}

  inline double Sigma() const {return sigma_;}
  inline void Sigma(double sigma) {sigma_=sigma;}

  inline void DetId(RPDetId det_id) {det_id_=det_id;}
  inline unsigned int DetId() const {return det_id_;}

  inline RPRecoHit *clone() const {return new RPRecoHit(*this); }

 private:
  RPDetId det_id_;    ///< the raw ID of detector
  double position_;   ///< position of the hit in mm, wrt detector center (see RPTopology::GetHitPositionInReadoutDirection)
  double sigma_;      ///< position uncertainty, in mm
};


inline bool operator<(const RPRecoHit &in1, const RPRecoHit &in2)
{
  if(in1.DetId() < in2.DetId())
    return true;
  else if(in1.DetId() == in2.DetId())
    return in1.Position() < in2.Position();
  else 
    return false;
}

#endif  //DataFormats_TotemRPDataTypes_RPRecoHit_h_

