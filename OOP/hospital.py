class Patient(object):
    self_id = 1
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.id = Patient.self_id
        Patient.self_id += 1
    def info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            print "{}: {}".format(attr, val)
        print "#" * 20

class Hospital(object):
    def __init__(self, name, capacity):
        self.patient_list = []
        self.bed_assigned = []
        self.queue_size = 0
        for i in range(0,capacity):
            self.bed_assigned.append(0)
        self.name = name
        self.capacity = capacity
    def add(self, patient):
        if (len(self.patient_list) >= self.capacity):
            print "Hospital is full, no space for {}, id:{}".format(patient.name, patient.id)
        else:
            x = 0
            while self.bed_assigned[x] == 1:
                x += 1
            patient.bed_number = x
            self.bed_assigned[x] = 1
            self.patient_list.append(patient)
            self.queue_size += 1
            print "Admission is complete for {}, id:{}, bed number:{}".format(patient.name, patient.id, patient.bed_number)
        return self
    def discharge(self, patient):
        for i in range(0,len(self.patient_list)):
            if (patient.id == self.patient_list[i].id):
                self.patient_list.pop(i)
                NUM = patient.bed_number
                self.bed_assigned[NUM] = 0
                self.queue_size -= 1
                break
        return self
    def display_info(self):
        for patient in self.patient_list:
            print "Name: {}, Bed#: {}".format(patient.name, patient.bed_number)
        print "Patient list size: {}".format(self.queue_size)
