#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>
#include <gazebo/common/Events.hh>
#include <gazebo/common/Assert.hh>

namespace gazebo
{
  class ModelPush : public ModelPlugin
  {
    public: void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
      // Store the pointer to the model
      this->model = _parent;

      // Listen to the update event. This event is broadcast every
      // simulation iteration.
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          std::bind(&ModelPush::OnUpdate, this, std::placeholders::_1));
    }


    // Called by the world update start event

    public: void OnUpdate(const common::UpdateInfo &_info)
    {

	if (_info.simTime <10 || _info.simTime>15 && _info.simTime <25 )
	{      
	      	this->model->SetLinearVel(ignition::math::Vector3d(.3, 0, 0));
		this->model->SetAngularVel(ignition::math::Vector3d(0, 0, 0));
	
	}


    }

    // Pointer to the model
    private: physics::ModelPtr model;

    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;
  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(ModelPush)
}

