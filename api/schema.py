from calendar import c
import graphene
from graphene_django import DjangoObjectType
from .models import UserProfile, User, Driver, Vehicle, Client, Trip, Merchandise, Container, Vidange, Panne, Maintenance, Entretien
from graphql_jwt.decorators import login_required, staff_member_required
from graphene_gis.converter import scalars

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = '__all__'

class DriverType(DjangoObjectType):
    class Meta:
        model = Driver
        fields = '__all__'

class VehicleType(DjangoObjectType):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = '__all__'

class TripType(DjangoObjectType):
    class Meta:
        model = Trip
        fields = '__all__'

class MerchandiseType(DjangoObjectType):
    class Meta:
        model = Merchandise
        fields = '__all__'

class ContainerType(DjangoObjectType):
    class Meta:
        model = Container
        fields = '__all__'

class VidangeType(DjangoObjectType):
    class Meta:
        model = Vidange
        fields = '__all__'

class PanneType(DjangoObjectType):
    class Meta:
        model = Panne
        fields = '__all__'
        
class MaintenanceType(DjangoObjectType):
    class Meta:
        model = Maintenance
        fields = '__all__'

class EntretienType(DjangoObjectType):
    class Meta:
        model = Entretien
        fields = '__all__'
        
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    user_profile = graphene.Field(UserProfileType, id=graphene.Int())
    drivers = graphene.List(DriverType)
    driver = graphene.Field(DriverType, id=graphene.Int())
    vehicles = graphene.List(VehicleType)
    vehicle = graphene.Field(VehicleType, id=graphene.Int())
    clients = graphene.List(ClientType)
    client = graphene.Field(ClientType, id=graphene.Int())
    trips = graphene.List(TripType)
    trip = graphene.Field(TripType, id=graphene.Int())
    merchandises = graphene.List(MerchandiseType)
    merchandise = graphene.Field(MerchandiseType, id=graphene.Int())
    containers = graphene.List(ContainerType)
    container = graphene.Field(ContainerType, id=graphene.Int())
    vidanges = graphene.List(VidangeType)
    vidange = graphene.Field(VidangeType, id=graphene.Int())
    pannes = graphene.List(PanneType)
    panne = graphene.Field(PanneType, id=graphene.Int())
    maintenances = graphene.List(MaintenanceType)
    maintenance = graphene.Field(MaintenanceType, id=graphene.Int())
    entretiens = graphene.List(EntretienType)
    entretien = graphene.Field(EntretienType, id=graphene.Int())

    @staff_member_required
    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    staff_member_required
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return User.objects.get(pk=id)
        return None
    
    @login_required
    def resolve_user_profile(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return UserProfile.objects.get(pk=id)
        return None
    
    @login_required
    def resolve_drivers(self, info, **kwargs):
        return Driver.objects.all()
    
    @login_required
    def resolve_driver(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Driver.objects.get(pk=id)
        return None
    
    @login_required
    def resolve_vehicles(self, info, **kwargs):
        return Vehicle.objects.all()
    
    @login_required
    def resolve_vehicle(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Vehicle.objects.get(pk=id)
    
    @login_required
    def resolve_clients(self, info, **kwargs):
        return Client.objects.all()

    @login_required
    def resolve_client(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Client.objects.get(pk=id)
        return None

    @login_required
    def resolve_trips(self, info, **kwargs):
        return Trip.objects.all()

    @login_required
    def resolve_trip(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Trip.objects.get(pk=id)
        return None

    @login_required
    def resolve_merchandises(self, info, **kwargs):
        return Merchandise.objects.all()

    @login_required
    def resolve_merchandise(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Merchandise.objects.get(pk=id)
        return None

    @login_required
    def resolve_containers(self, info, **kwargs):
        return Container.objects.all()

    @login_required
    def resolve_container(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Container.objects.get(pk=id)
        return None

    @login_required
    def resolve_vidanges(self, info, **kwargs):
        return Vidange.objects.all()

    @login_required
    def resolve_vidange(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Vidange.objects.get(pk=id)
        return None

    @login_required
    def resolve_pannes(self, info, **kwargs):
        return Panne.objects.all()

    @login_required
    def resolve_panne(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Panne.objects.get(pk=id)
        return None

    @login_required
    def resolve_maintenances(self, info, **kwargs):
        return Maintenance.objects.all()

    @login_required
    def resolve_maintenance(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Maintenance.objects.get(pk=id)
        return None

    @login_required
    def resolve_entretiens(self, info, **kwargs):
        return Entretien.objects.all()

    @login_required
    def resolve_entretien(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Entretien.objects.get(pk=id)
        return None

    whoami = graphene.Field(UserType, token=graphene.String(required=True))

    @login_required
    def resolve_whoami(self, info, **kwargs):
        return info.context.user

class VehicleInput(graphene.InputObjectType):
    id = graphene.ID()
    vehicle_number = graphene.String()
    vehicle_type = graphene.String()
    vehicle_model = graphene.String()
    vehicle_capacity_quantity = graphene.Float()
    vehicle_capacity_unit = graphene.String()
    vehicule_mileage = graphene.Float()

class MerchandiseInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    type = graphene.String()
    client = graphene.ID()
    weight_quantity = graphene.Float()
    weight_unit = graphene.String()
    volume_quantity = graphene.Float()
    volume_unit = graphene.String()

class ContainerInput(graphene.InputObjectType):
    id = graphene.ID()
    container_number = graphene.String()
    container_type = graphene.String()
    container_capacity_quantity = graphene.Float()
    container_capacity_unit = graphene.String()

class TripInput(graphene.InputObjectType):
    id = graphene.ID()
    driver = graphene.ID()
    vehicle = graphene.ID()
    container = graphene.ID()
    merchandises = graphene.List(MerchandiseInput)
    origin = graphene.Field(graphene.String, to=scalars.PointScalar())
    destination = graphene.Field(graphene.String, to=scalars.PointScalar())
    distance = graphene.Float()
    actual_position = graphene.Field(graphene.String, to=scalars.PointScalar())
    status = graphene.String()
    departure_date = graphene.DateTime()
    arrival_date = graphene.DateTime()
    consumption = graphene.Float()
    driver_price = graphene.Float()
    client_price = graphene.Float()

class VidangeInput(graphene.InputObjectType):
    id = graphene.ID()
    vehicle = graphene.ID()
    date = graphene.DateTime()
    mileage = graphene.Float()
    note = graphene.String()
    price = graphene.Float()

class PanneInput(graphene.InputObjectType):
    id = graphene.ID()
    vehicle = graphene.ID()
    driver = graphene.ID()
    description = graphene.String()
    date = graphene.DateTime()
    mileage = graphene.Float()

class MaintenanceInput(graphene.InputObjectType):
    id = graphene.ID()
    vehicle = graphene.ID()
    pannes = graphene.List(PanneInput)
    note = graphene.String()
    date = graphene.DateTime()
    mileage = graphene.Float()
    price = graphene.Float()

class EntretienInput(graphene.InputObjectType):
    id = graphene.ID()
    vehicle = graphene.ID()
    date = graphene.DateTime()
    remarks = graphene.String()

class CreateVehicle(graphene.Mutation):
    class Arguments:
        input = VehicleInput(required=True)

    ok = graphene.Boolean()
    vehicle = graphene.Field(VehicleType)

    @login_required
    def mutate(self, info, input=None):
        vehicle = Vehicle(
            vehicle_number=input.vehicle_number,
            vehicle_type=input.vehicle_type,
            vehicle_model=input.vehicle_model,
            vehicle_capacity_quantity=input.vehicle_capacity_quantity,
            vehicle_capacity_unit=input.vehicle_capacity_unit,
            vehicule_mileage=input.vehicule_mileage
        )
        vehicle.save()
        ok = True
        return CreateVehicle(vehicle=vehicle, ok=ok)

class UpdateVehicle(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = VehicleInput(required=True)

    ok = graphene.Boolean()
    vehicle = graphene.Field(VehicleType)

    @login_required
    def mutate(self, info, id, input=None):
        vehicle = Vehicle.objects.get(pk=id)
        if vehicle:
            vehicle.vehicle_number = input.vehicle_number
            vehicle.vehicle_type = input.vehicle_type
            vehicle.vehicle_model = input.vehicle_model
            vehicle.vehicle_capacity_quantity = input.vehicle_capacity_quantity
            vehicle.vehicle_capacity_unit = input.vehicle_capacity_unit
            vehicle.vehicule_mileage = input.vehicule_mileage
            vehicle.save()
            ok = True
            return UpdateVehicle(vehicle=vehicle, ok=ok)
        return UpdateVehicle(vehicle=None, ok=False)

class DeleteVehicle(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        vehicle = Vehicle.objects.get(pk=id)
        if vehicle:
            vehicle.delete()
            ok = True
            return DeleteVehicle(ok=ok)
        return DeleteVehicle(ok=False)

class CreateMerchandise(graphene.Mutation):
    class Arguments:
        input = MerchandiseInput(required=True)

    ok = graphene.Boolean()
    merchandise = graphene.Field(MerchandiseType)

    @login_required
    def mutate(self, info, input=None):
        merchandise = Merchandise(
            name=input.name,
            type=input.type,
            client=input.client,
            weight_quantity=input.weight_quantity,
            weight_unit=input.weight_unit,
            volume_quantity=input.volume_quantity,
            volume_unit=input.volume_unit
        )
        merchandise.save()
        ok = True
        return CreateMerchandise(merchandise=merchandise, ok=ok)

class UpdateMerchandise(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = MerchandiseInput(required=True)

    ok = graphene.Boolean()
    merchandise = graphene.Field(MerchandiseType)

    @login_required
    def mutate(self, info, id, input=None):
        merchandise = Merchandise.objects.get(pk=id)
        if merchandise:
            merchandise.name = input.name
            merchandise.type = input.type
            merchandise.client = input.client
            merchandise.weight_quantity = input.weight_quantity
            merchandise.weight_unit = input.weight_unit
            merchandise.volume_quantity = input.volume_quantity
            merchandise.volume_unit = input.volume_unit
            merchandise.save()
            ok = True
            return UpdateMerchandise(merchandise=merchandise, ok=ok)
        return UpdateMerchandise(merchandise=None, ok=False)

class DeleteMerchandise(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        merchandise = Merchandise.objects.get(pk=id)
        if merchandise:
            merchandise.delete()
            ok = True
            return DeleteMerchandise(ok=ok)
        return DeleteMerchandise(ok=False)

class CreateContainer(graphene.Mutation):
    class Arguments:
        input = ContainerInput(required=True)

    ok = graphene.Boolean()
    container = graphene.Field(ContainerType)

    @login_required
    def mutate(self, info, input=None):
        container = Container(
            container_number=input.container_number,
            container_type=input.container_type,
            container_capacity_quantity=input.container_capacity_quantity,
            container_capacity_unit=input.container_capacity_unit
        )
        container.save()
        ok = True
        return CreateContainer(container=container, ok=ok)

class UpdateContainer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ContainerInput(required=True)

    ok = graphene.Boolean()
    container = graphene.Field(ContainerType)

    @login_required
    def mutate(self, info, id, input=None):
        container = Container.objects.get(pk=id)
        if container:
            container.container_number = input.container_number
            container.container_type = input.container_type
            container.container_capacity_quantity = input.container_capacity_quantity
            container.container_capacity_unit = input.container_capacity_unit
            container.save()
            ok = True
            return UpdateContainer(container=container, ok=ok)
        return UpdateContainer(container=None, ok=False)

class DeleteContainer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        container = Container.objects.get(pk=id)
        if container:
            container.delete()
            ok = True
            return DeleteContainer(ok=ok)
        return DeleteContainer(ok=False)

class CreateTrip(graphene.Mutation):
    class Arguments:
        input = TripInput(required=True)

    ok = graphene.Boolean()
    trip = graphene.Field(TripType)

    @login_required
    def mutate(self, info, input=None):
        trip = Trip(
            driver=input.driver,
            vehicle=input.vehicle,
            container=input.container,
            merchandise=input.merchandise,
            origin=input.origin,
            destination=input.destination,
            distance = input.distance,
            actual_position = input.actual_position,
            status=input.status,
            departure_date=input.departure_date,
            arrival_date=input.arrival_date,
            consumption = input.consumption,
            driver_price = input.driver_price,
            client_price = input.client_price
        )
        trip.save()
        ok = True
        return CreateTrip(trip=trip, ok=ok)

class UpdateTrip(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = TripInput(required=True)

    ok = graphene.Boolean()
    trip = graphene.Field(TripType)

    @login_required
    def mutate(self, info, id, input=None):
        trip = Trip.objects.get(pk=id)
        if trip:
            trip.driver = input.driver
            trip.vehicle = input.vehicle
            trip.container = input.container
            trip.merchandise = input.merchandise
            trip.origin = input.origin
            trip.destination = input.destination
            trip.distance = input.distance
            trip.actual_position = input.actual_position
            trip.status = input.status
            trip.departure_date = input.departure_date
            trip.arrival_date = input.arrival_date
            trip.consumption = input.consumption
            trip.driver_price = input.driver_price
            trip.client_price = input.client_price
            trip.save()
            ok = True
            return UpdateTrip(trip=trip, ok=ok)
        return UpdateTrip(trip=None, ok=False)

class DeleteTrip(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        trip = Trip.objects.get(pk=id)
        if trip:
            trip.delete()
            ok = True
            return DeleteTrip(ok=ok)
        return DeleteTrip(ok=False)

class CreateVidange(graphene.Mutation):
    class Arguments:
        input = VidangeInput(required=True)

    ok = graphene.Boolean()
    vidange = graphene.Field(VidangeType)

    @login_required
    def mutate(self, info, input=None):
        vidange = Vidange(
            vehicle=input.vehicle,
            date=input.date,
            mileage=input.mileage,
            price=input.price,
            note=input.note
        )
        vidange.save()
        ok = True
        return CreateVidange(vidange=vidange, ok=ok)

class UpdateVidange(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = VidangeInput(required=True)

    ok = graphene.Boolean()
    vidange = graphene.Field(VidangeType)

    @login_required
    def mutate(self, info, id, input=None):
        vidange = Vidange.objects.get(pk=id)
        if vidange:
            vidange.vehicle = input.vehicle
            vidange.date = input.date
            vidange.mileage = input.mileage
            vidange.price = input.price
            vidange.note = input.note
            vidange.save()
            ok = True
            return UpdateVidange(vidange=vidange, ok=ok)
        return UpdateVidange(vidange=None, ok=False)

class DeleteVidange(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        vidange = Vidange.objects.get(pk=id)
        if vidange:
            vidange.delete()
            ok = True
            return DeleteVidange(ok=ok)
        return DeleteVidange(ok=False)

class CreatePanne(graphene.Mutation):
    class Arguments:
        input = PanneInput(required=True)

    ok = graphene.Boolean()
    panne = graphene.Field(PanneType)

    @login_required
    def mutate(self, info, input=None):
        panne = Panne(
            vehicle=input.vehicle,
            driver=input.driver,
            date=input.date,
            mileage=input.mileage,
            description=input.note
        )
        panne.save()
        ok = True
        return CreatePanne(panne=panne, ok=ok)

class UpdatePanne(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = PanneInput(required=True)

    ok = graphene.Boolean()
    panne = graphene.Field(PanneType)

    @login_required
    def mutate(self, info, id, input=None):
        panne = Panne.objects.get(pk=id)
        if panne:
            panne.vehicle = input.vehicle
            panne.driver = input.driver
            panne.date = input.date
            panne.mileage = input.mileage
            panne.description = input.note
            panne.save()
            ok = True
            return UpdatePanne(panne=panne, ok=ok)
        return UpdatePanne(panne=None, ok=False)

class DeletePanne(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        panne = Panne.objects.get(pk=id)
        if panne:
            panne.delete()
            ok = True
            return DeletePanne(ok=ok)
        return DeletePanne(ok=False)
    
class CreateMaintenance(graphene.Mutation):
    class Arguments:
        input = MaintenanceInput(required=True)

    ok = graphene.Boolean()
    maintenance = graphene.Field(MaintenanceType)

    @login_required
    def mutate(self, info, input=None):
        maintenance = Maintenance(
            vehicle=input.vehicle,
            pannes=input.pannes,
            note=input.note,
            date=input.date,
            mileage=input.mileage,
            price=input.price
        )
        maintenance.save()
        ok = True
        return CreateMaintenance(maintenance=maintenance, ok=ok)

class UpdateMaintenance(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = MaintenanceInput(required=True)

    ok = graphene.Boolean()
    maintenance = graphene.Field(MaintenanceType)

    @login_required
    def mutate(self, info, id, input=None):
        maintenance = Maintenance.objects.get(pk=id)
        if maintenance:
            maintenance.vehicle = input.vehicle
            maintenance.pannes = input.pannes
            maintenance.note = input.note
            maintenance.date = input.date
            maintenance.mileage = input.mileage
            maintenance.price = input.price
            maintenance.save()
            ok = True
            return UpdateMaintenance(maintenance=maintenance, ok=ok)
        return UpdateMaintenance(maintenance=None, ok=False)

class DeleteMaintenance(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        maintenance = Maintenance.objects.get(pk=id)
        if maintenance:
            maintenance.delete()
            ok = True
            return DeleteMaintenance(ok=ok)
        return DeleteMaintenance(ok=False)

class CreateEntretien(graphene.Mutation):
    class Arguments:
        input = EntretienInput(required=True)

    ok = graphene.Boolean()
    entretien = graphene.Field(EntretienType)

    @login_required
    def mutate(self, info, input=None):
        entretien = Entretien(
            vehicle=input.vehicle,
            date=input.date,
            remarks=input.mileage
        )
        entretien.save()
        ok = True
        return CreateEntretien(entretien=entretien, ok=ok)

class UpdateEntretien(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = EntretienInput(required=True)

    ok = graphene.Boolean()
    entretien = graphene.Field(EntretienType)

    @login_required
    def mutate(self, info, id, input=None):
        entretien = Entretien.objects.get(pk=id)
        if entretien:
            entretien.vehicle = input.vehicle
            entretien.date = input.date
            entretien.remarks = input.mileage
            entretien.save()
            ok = True
            return UpdateEntretien(entretien=entretien, ok=ok)
        return UpdateEntretien(entretien=None, ok=False)

class DeleteEntretien(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        entretien = Entretien.objects.get(pk=id)
        if entretien:
            entretien.delete()
            ok = True
            return DeleteEntretien(ok=ok)
        return DeleteEntretien(ok=False)

class Mutation(graphene.ObjectType):
    create_vehicle = CreateVehicle.Field()
    update_vehicle = UpdateVehicle.Field()
    delete_vehicle = DeleteVehicle.Field()
    create_trip = CreateTrip.Field()
    update_trip = UpdateTrip.Field()
    delete_trip = DeleteTrip.Field()
    create_merchandise = CreateMerchandise.Field()
    update_merchandise = UpdateMerchandise.Field()
    delete_merchandise = DeleteMerchandise.Field()
    create_container = CreateContainer.Field()
    update_container = UpdateContainer.Field()
    delete_container = DeleteContainer.Field()
    create_vidange = CreateVidange.Field()
    update_vidange = UpdateVidange.Field()
    delete_vidange = DeleteVidange.Field()
    create_panne = CreatePanne.Field()
    update_panne = UpdatePanne.Field()
    delete_panne = DeletePanne.Field()
    create_maintenance = CreateMaintenance.Field()
    update_maintenance = UpdateMaintenance.Field()
    delete_maintenance = DeleteMaintenance.Field()
    create_entretien = CreateEntretien.Field()
    update_entretien = UpdateEntretien.Field()
    delete_entretien = DeleteEntretien.Field()
